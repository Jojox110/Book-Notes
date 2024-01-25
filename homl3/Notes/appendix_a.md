# Machine learning project checklist

## 1) Frame the problem and look at the big picture
- 1) Define the objective in buisness terms
- 2) How will your solutions be used?
- 3) What are the current solutions/workarounds (if any)
- 4) How should you frame this problem (supervised/unsupervised, online/offline, ...)
- 5) How should performance be measured?
- 6) Is the performance measure aligned with the buiness objectives?
- 7) What would be the minimum performance needed to reach the buisness objective?
- 8) What are comparable problems? Can you reuse experience or tools?
- 9) Is human expertise available?
- 10) How would you solve the problem manually?
- 11) List the assumptions you (or others) have made to far
- 12) Verify assumptions if possible

## 2) Get the data
Note: Automate as much as possible

- 1) List the data you need and how much you need
- 2) Find and document where you can get that data
- 3) Check how much space it will take
- 4) Check legal obligations, and get authorization if necessary
- 5) Get access authorizations
- 6) Create a workspace (with enough storage space)
- 7) Get the data
- 8) Convert the data to a format you can easily manipulate (without changing the data itself)
- 9) Ensure sensitive information is deleted or protected (ex: anonymized)
- 10) check the size and type of data
- 11) Sample a test set, put it aside, and never look at it

## 3) Explore the data to gain insight
Note: Try to get insights from a field expert for these steps

- 1) Create a copy of the data for exploration
- 2) Create a Jupyter notebook to keep a record of your data exploration
- 3) Study each attribute and its characteristics
- 4) For supervised learning, identify the target attributes
- 5) Visualize the data
- 6) Study the correlations between attributes
- 7) Study how you would solve the problems manually
- 8) Identify the promising transofmrations you may want to apply
- 9) Identify extra data that would be useful
- 10) Document what you have learned

## 4) Prepare the data to better expore the underlying data patterns to machine learning algorithmns
Note: Work on copies of the data and write functions for data transformations

- 1) Clean the data
- 2) Perform feature selection
- 3) Perform feature engineering where appropriate
- 4) Perform feature scaling

## 5) Explore many different models and shortlist the best ones
Note: we can use sample sets of training data, but see consequences of doing so before 

- 1) Train many quick and dirty models from different categories using standard parameters
- 2) Measure and compare their performance  (use N-fold cross-validation)
- 3) Analyze the most significant variables for each algorithm
- 4) analyze the types of errors the models make
- 5) Perform a quick round of feature selection and engineering
- 6) Perform one or two more quick iterations of the five previous steps
- 7) Shortlist the top three to five most promising models, perferring models that make different types of errors

## 6) Fine-tune your models and combine them into a great solution
Note: Use as much data as possible

- 1) Fine-tune the hyperparameters using cross-validation
- 2) Try ensemble methods. Combining your best models will often produce better performance than running them individually
- 3) Once you are confident about your final model, measure ites performance on the test set to estimate the generalization error

## 7) Present your solution

- 1) Document what you have done
- 2) Create a nice presentation
- 3) Explain why your solution achieves the buisness objective
- 4) Don't forget present interesting points you noticed along the way
- 5) Ensure your key findings are communicated through beatiful visualizations or easy to remember statements

## 8) Launch, monitor, and maintain your system

- 1) Get your solution ready for production
- 2) Write monitoring code to check your system's live performance at regular intervals and trigger alerts when it drops
- 3) Retrain your models on a regular basis on fresh data