## Python 的全局锁问题
尽管 Python 完全支持多线程编程，但是解释器的 C 语言实现部分在完全并行执行
时并不是线程安全的。实际上，解释器被一个全局解释器锁保护着，它确保任何时候
都只有一个 Python 线程执行。 `GIL` 最大的问题就是 Python 的多线程程序并不能利用
多核 CPU 的优势（比如一个使用了多个线程的计算密集型程序只会在一个单 CPU 上
面运行）。

在讨论普通的 GIL 之前，有一点要强调的是 GIL 只会影响到那些严重依赖 CPU
的程序（比如计算型的）。如果你的程序大部分只会设计到 I/O，比如网络交互，那么
使用多线程就很合适，因为它们大部分时间都在等待。实际上，你完全可以放心的创
建几千个 Python 线程，现代操作系统运行这么多线程没有任何压力，没啥可担心的。

而对于依赖 CPU 的程序，你需要弄清楚执行的计算的特点。例如，优化底层算法
要比使用多线程运行快得多。类似的，由于 Python 是解释执行的，如果你将那些性能
瓶颈代码移到一个 C 语言扩展模块中，速度也会提升的很快。如果你要操作数组，那
么使用 NumPy 这样的扩展会非常的高效。最后，你还可以考虑下其他可选实现方案，
比如 PyPy，它通过一个 JIT 编译器来优化执行效率

还有一点要注意的是，线程不是专门用来优化性能的。一个 CPU 依赖型程序可能
会使用线程来管理一个图形用户界面、一个网络连接或其他服务。这时候， GIL 会产
生一些问题，因为如果一个线程长期持有 GIL 的话会导致其他非 CPU 型线程一直等
待。事实上，一个写的不好的 C 语言扩展会导致这个问题更加严重，尽管代码的计算
部分会比之前运行的更快些。

说了这么多，现在想说的是我们有两种策略来解决 GIL 的缺点。首先，如果你完
全工作于 Python 环境中，你可以使用 multiprocessing 模块来创建一个进程池，并
像协同处理器一样的使用它。例如，加入你有如下的线程代码：

```python
# Performs a large calculation (CPU bound)
def some_work(args):
    ...
    return result
# A thread that calls the above function
def some_thread():
    while True:
        ...
        r = some_work(args)
```
修改代码，使用进程池：
```python
# Processing pool (see below for initiazation)
pool = None
# Performs a large calculation (CPU bound)
def some_work(args):
    ...
    return result
# A thread that calls the above function
def some_thread():
    while True:
        ...
        r = pool.apply(some_work, (args))
        ...
# Initiaze the pool
if __name__ == '__main__':
    import multiprocessing
    pool = multiprocessing.Pool()
```
这个通过使用一个技巧利用进程池解决了 `GIL` 的问题。当一个线程想要执行 CPU
密集型工作时，会将任务发给进程池。然后进程池会在另外一个进程中启动一个单独
的 Python 解释器来工作。当线程等待结果的时候会释放 GIL。并且，由于计算任务在
单独解释器中执行，那么就不会受限于 `GIL` 了。在一个多核系统上面，你会发现这个
技术可以让你很好的利用多 CPU 的优势

另外一个解决 GIL 的策略是使用 C 扩展编程技术。主要思想是将计算密集型任务
转移给 C，跟 Python 独立，在工作的时候在 C 代码中释放 GIL。这可以通过在 C 代
码中插入下面这样的特殊宏来完成：
```c
#include "Python.h"
...
PyObject *pyfunc(PyObject *self, PyObject *args) {
    ...
    Py_BEGIN_ALLOW_THREADS
    // Threaded C code
    ...
    Py_END_ALLOW_THREADS
    ...
}
```
如果你使用其他工具访问 C 语言，比如对于 Cython 的 ctypes 库，你不需要做任
何事。例如， ctypes 在调用 C 时会自动释放 GIL。

许多程序员在面对线程性能问题的时候，马上就会怪罪 GIL，什么都是它的问题。
其实这样子太不厚道也太天真了点。作为一个真实的例子，在多线程的网络编程中神
秘的 stalls 可能是因为其他原因比如一个 DNS 查找延时，而跟 GIL 毫无关系。最后
你真的需要先去搞懂你的代码是否真的被 GIL 影响到。同时还要明白 GIL 大部分都应
该只关注 CPU 的处理而不是 I/O.

如果你准备使用一个处理器池，注意的是这样做涉及到数据序列化和在不同
Python 解释器通信。被执行的操作需要放在一个通过 def 语句定义的 Python 函数
中，不能是 lambda、闭包可调用实例等，并且函数参数和返回值必须要兼容 pickle。
同样，要执行的任务量必须足够大以弥补额外的通宵开销。

另外一个难点是当混合使用线程和进程池的时候会让你很头疼。如果你要同时使用
两者，最好在程序启动时，创建任何线程之前先创建一个单例的进程池。然后线程使
用同样的进程池来进行它们的计算密集型工作。

C 扩展最重要的特征是它们和 Python 解释器是保持独立的。也就是说，如果你准
备将 Python 中的任务分配到 C 中去执行，你需要确保 C 代码的操作跟 Python 保持
独立，这就意味着不要使用 Python 数据结构以及不要调用 Python 的 C API。另外一
个就是你要确保 C 扩展所做的工作是足够的，值得你这样做。也就是说 C 扩展担负起
了大量的计算任务，而不是少数几个计算。

这些解决 GIL 的方案并不能适用于所有问题。例如，某些类型的应用程序如果被
分解为多个进程处理的话并不能很好的工作，也不能将它的部分代码改成 C 语言执行。
对于这些应用程序，你就要自己需求解决方案了（比如多进程访问共享内存区，多解
析器运行于同一个进程等）。或者，你还可以考虑下其他的解释器实现，比如 PyPy。