"""

Generator Functions and Expressions
Python today supports procrastination much more than it did in the past—it provides
tools that produce results only when needed, instead of all at once. We’ve seen this at
work in built-in tools: files that read lines on request, and functions like map and zip
that produce items on demand in 3.X. Such laziness isn’t confined to Python itself,
though. In particular, two language constructs delay result creation whenever possible
in user-defined operations:
• Generator functions (available since 2.3) are coded as normal def statements, but
use yield statements to return results one at a time, suspending and resuming their
state between each.
• Generator expressions (available since 2.4) are similar to the list comprehensions
of the prior section, but they return an object that produces results on demand
instead of building a result list.
Because neither constructs a result list all at once, they save memory space and allow
computation time to be split across result requests. As we’ll see, both of these ultimately
perform their delayed-results magic by implementing the iteration protocol we studied
in Chapter 14.
These features are not new (generator expressions were available as an option as early
as Python 2.2), and are fairly common in Python code today. Python’s notion of generators
owes much to other programming languages, especially Icon. Though they may
initially seem unusual if you’re accustomed to simpler programming models, you’ll
probably find generators to be a powerful tool where applicable. Moreover, because
they are a natural extension to the function, comprehension, and iteration ideas we’ve
Generator Functions and Expressions | 591
www.it-ebooks.info
already explored, you already know more about coding generators than you might
expect.
Generator Functions: yield Versus return
In this part of the book, we’ve learned about coding normal functions that receive input
parameters and send back a single result immediately. It is also possible, however, to
write functions that may send back a value and later be resumed, picking up where they
left off. Such functions, available in both Python 2.X and 3.X, are known as generator
functions because they generate a sequence of values over time.
Generator functions are like normal functions in most respects, and in fact are coded
with normal def statements. However, when created, they are compiled specially into
an object that supports the iteration protocol. And when called, they don’t return a
result: they return a result generator that can appear in any iteration context. We studied
iterables in Chapter 14, and Figure 14-1 gave a formal and graphic summary of their
operation. Here, we’ll revisit them to see how they relate to generators.
State suspension
Unlike normal functions that return a value and exit, generator functions automatically
suspend and resume their execution and state around the point of value generation.
Because of that, they are often a useful alternative to both computing an entire series
of values up front and manually saving and restoring state in classes. The state that
generator functions retain when they are suspended includes both their code location,
and their entire local scope. Hence, their local variables retain information between
results, and make it available when the functions are resumed.
The chief code difference between generator and normal functions is that a generator
yields a value, rather than returning one—the yield statement suspends the function
and sends a value back to the caller, but retains enough state to enable the function to
resume from where it left off. When resumed, the function continues execution immediately
after the last yield run. From the function’s perspective, this allows its code
to produce a series of values over time, rather than computing them all at once and
sending them back in something like a list.
Iteration protocol integration
To truly understand generator functions, you need to know that they are closely bound
up with the notion of the iteration protocol in Python. As we’ve seen, iterator objects
define a __next__ method (next in 2.X), which either returns the next item in the iteration,
or raises the special StopIteration exception to end the iteration. An iterable
object’s iterator is fetched initially with the iter built-in function, though this step is a
no-op for objects that are their own iterator.
592 | Chapter 20: Comprehensions and Generations
www.it-ebooks.info
Python for loops, and all other iteration contexts, use this iteration protocol to step
through a sequence or value generator, if the protocol is supported (if not, iteration
falls back on repeatedly indexing sequences instead). Any object that supports this
interface works in all iteration tools.
To support this protocol, functions containing a yield statement are compiled specially
as generators—they are not normal functions, but rather are built to return an object
with the expected iteration protocol methods. When later called, they return a generator
object that supports the iteration interface with an automatically created method
named __next__ to start or resume execution.
Generator functions may also have a return statement that, along with falling off the
end of the def block, simply terminates the generation of values—technically, by raising
a StopIteration exception after any normal function exit actions. From the caller’s
perspective, the generator’s __next__ method resumes the function and runs until either
the next yield result is returned or a StopIteration is raised.
The net effect is that generator functions, coded as def statements containing yield
statements, are automatically made to support the iteration object protocol and thus
may be used in any iteration context to produce results over time and on demand.
As noted in Chapter 14, in Python 2.X, iterator objects define a method
named next instead of __next__. This includes the generator objects we
are using here. In 3.X this method is renamed to __next__. The next
built-in function is provided as a convenience and portability tool:
next(I) is the same as I.__next__() in 3.X and I.next() in 2.6 and 2.7.
Prior to 2.6, programs simply call I.next() instead to iterate manually.
Generator functions in action
To illustrate generator basics, let’s turn to some code. The following code defines a
generator function that can be used to generate the squares of a series of numbers over
time:
>>> def gensquares(N):
for i in range(N):
yield i ** 2 # Resume here later
This function yields a value, and so returns to its caller, each time through the loop;
when it is resumed,
"""