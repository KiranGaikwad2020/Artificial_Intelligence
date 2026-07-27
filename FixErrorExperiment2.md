# Rule Based Program Execution Process

Step 1: Run the program on terminal with the command **$ python3 programname**

Step 2: If following error found

-  ![Frozendict Execution Error ](images/Exp2ExecutionErrorResolutionImages/RuleBasedCodeExecutionError.png)

Step 3: Resolve the issue as follows:

- Remove the previous installed version of **frondict** and **experta** as follows
  
- ![Frozendict Uninstall ](images/Exp2ExecutionErrorResolutionImages/FrozenDict-ExpertaRemovalCOmmand.png)

- Reinstall the required version of **frozendict** as follows

- ![Frozendict Install ](images/Exp2ExecutionErrorResolutionImages/Frozendict2.3.4._InstallationCommand.png)

- Use the **experta** instalaltion command as above replacing **frondict**
- -- Also make the changes as follows:
- gedit /home/ai-114/.local/lib/python3.10/site-packages/experta/__init__.py
- And add import collections.abc and and after 4-5 line also add in function argument(collections.abc.Mapping instead of collections.Mapping)

Step 4: Python code to be tested is as follows:

- ![Rule based Code ](images/Exp2ExecutionErrorResolutionImages/RuleBAsedCode.png)
