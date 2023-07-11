# Python async function

# Resources
- [Async IO in Python: A Complete Walkthrough](https://intranet.alxswe.com/rltoken/zYkXScziW1D5rNdNEvObjQ)
- [asyncio - Asynchronous I/O](https://intranet.alxswe.com/rltoken/aZUO4GiWHbPIrVBIwptFAw)
- [random.uniform](https://intranet.alxswe.com/rltoken/72mVf1s8rx2ih_U2WjBmaA)

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- async and await syntax
- How to execute an async program with asyncio
- How to run concurrent coroutines
- How to create asyncio tasks
- How to use the random module

# async programming - terms to remember
Asynchronous programming is language agnostic (i.e it's a principle or concept that is applicable in any programming langugae. it is not constrained to a particular programming language).

## concepts related to asynchronous programming (Note: what I have here are my thoughts)
**Parallelism:**
    The ability to run a stream of programs(processes) simultaneously. From the world parallel, Each process doesn't hinder the other process.

**Multiprocessing:**
    A way of implementing parallelism. Multiprocessing employs the concept of parallelism to execute multiple tasks. One catch is that this tasks must be CPU bound (i.e Tasks that require the central processing
    involvement). The most common tasks/programs/processes that fall under this are Games, video and image editing e.t.c

**Threading:**
    Threading is a subset of Multiprocessing. Let's take a real life illustration outside the world of programming. Take the goverment of a nation for example. The goverment is carrys out a load of activities around the country. Each of these activities are executed individually by sub-sections of the goverment. This is multiprocessing at the highest level. Now each of these sub-sections also have smaller activities as well that contribute to the entire output from each sub-section. This is threading at sub-section level. Each sub-section can run multiple activities (threads) within themselves inorder to achieve the task given to them from the highest level of authority. Threading is more inclined towards IO(input/Output) tasks while Multiprocessing is inclined towards CPU bound tasks. 

    `Multiprocessing is like a parent folder with multiple processes which are child folders inside the paraent folder. Threads are like files inside the children folder.`

**Concurrency**
    A concept that multiple processes running together can overlap. A process that starts last can finish ealier than one that started first. processes execute in no particular order interms of when they started, ran and completed. So generaly whenever you talk about threading, you are implying concurrency and whenever you talk about multiprocessing, you are implying parallelism. You can have series of tabs opened on a particular browser like firefox and have them load up their contents in no particular order.


## The asyncio library in python
**coroutine:**
    A wrapped version of a normal function in python.
    This is a coroutine:

    ```py
    async def main():
        pass
    ```
**async event-loop:**
    asyncio.run allows us run a coroutine

    ```py 
    asyncio.run(main())
    ```


