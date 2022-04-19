# Simulated-Annealing-Deals-with-Flow-Shop-Schedual-Problem
北京理工大学最优化方法作业



代码的环境已经在实验报告中说明，下面再说一些运行问题：
1.	代码读入的是老师给的文件‘input.txt’，所以运行代码前请确保该文件与代码文件在同一文件夹下。也可以通过修改main中的路径，变为您电脑上的input.txt的文件路径来读入。 
2.	Simulate.py是和实验报告配套的代码，配套请看这个代码。
3.	Simulate_plus.py是能解出更优的解，但是运行时间过长的代码，具体原因如下：
Simulate.py中找到的解都是默认“每个机器上的工件顺序都一样”的，这样可以快速的找到一个不错的解，但为了找到更优解，simulate_plus.py这个代码可以做到“每个机器上的工件顺序可以不一样”。
4.	Tmp_best.txt中每个数据是每个机器都一样的一个加工工件顺序。
5.	Tmp_best_plus.txt中每个数据的排序从上到下，第i行是第i个机器上的工件顺序。
