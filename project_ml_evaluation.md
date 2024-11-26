#### SER594: Machine Learning Evaluation
#### (Analysis of 911 Calls)
#### (Sai Ganesh Nindra)
#### (11/25/2024)

## Evaluation Metrics
### Metric 1
**Name:** Mean Absolute Error (MAE)

**Choice Justification:** Simply put Mean Absolute Error is the go to metric for most regression models. With respect to my project it was an easy to understand metric
that helped me see how far off my model was in predicted dispatch times in minutes. The average error gives a basic sense of how many minutes in excess it is predicted,
in a case where the dispatch would have reached earlier or how much faster they will reach but in reality they would'nt, given the error of my model. So keeping it close to zero would be ideal.

Interpretation:** The Mean Absolute Error falls in an acceptable range over all three models I have implemented. About 0 - 5 minutes error is acceptable,
but there is scope for improvement, the features are very complex and about 97 features after encoding. There is no traffic data too, so a high MAE is inevitable. Given the domain of my project the ultimate aim should be to get an error as close to 0 as possible. Random Forest resulted in the least Mean Absolute Error. 

### Metric 2
**Name:** Root Mean Squared Error (MSE)

**Choice Justification:** Similar to MSE but it gives the root of the squared difference between the predicted time taken verse the actual time taken by dispatch. This metric
again helps me evaluate the model in a better way as it gives the error in the original metric that the target feature is in, that is minutes. Making it more readable and 
understandable and at the same time will give more weight to the large errors. 

Interpretation:** Given that XGBoost, Random Forest and Stacking Model has given a comparitively low Root Mean Squared Error, can mean that they handled the large errors well, but Ridge Regression
on the other hand gave a  larger value than the others indicating poor handling on large errors. 

### Metric 3
**Name:** R squared (R^2)

**Choice Justification:** Given that we are trying to predict the time taken by dispatch units, R squared is a measure that helps in explaining how well the target is varied.
A higher R squared generally depicts a model that is able to capture the complexities behind predicting a target and the patterns behind them.

Interpretation:** R squared depicts the ability to capture the variance in the data and it doesnt seem to have caught to any in Ridge Regression, which means that it is
not able to handle the complexities of predicting time taken. On the other hand XGBoost and Random Forest are able to explain much more variance comparitively. And one other
thing to notice is that Stacking Model is overall better in cases where large errors need to be handled well and have a good explainability of the variance.

## Alternative Models
### Alternative 1 Ridge 
**Construction:** Yes using a Ridge is not an ideal case here, like in XGBoost have taken care of overfitting as it uses L2 regularization. There is no scaling done here.
And yes like XGBoost have tuned the model to take a regularisation parameter to deal large coefficients.

**Evaluation:** The evaluation metrics of Ridge are the worst among the lot. High mean absolute and root mean squared error. Hence very poor accuracy in predicted the time taken. 
Moreover it has a very poor R squared value which almost deems the model not useful for this data. Explain very little variance and doesnt seem to have gotten along with the 
complex nature of the target variable.


### Alternative 2 Random Forest
**Construction:** XGBoost builds trees sequentially and focuses on rectifying errors in trees, whereas in Random Forest it builds multiple trees independently and averages 
it out. Unlike XGBoost scaling hasnt been done here. In XGBoost I tuned it with a learning rate and looked out for overfitting whereas in Random Forest I have gone for a simple
implementation but made it parralelised unlike XGBoost which works sequentially.

**Evaluation:** It has outperformed XGBoost in all error metrics I have chosen. This implies that it has captured the essence and complex nature of the target variable 
well. It shows more variance as well and can understand more than XGBoost (the relationship and patterns)


### Alternative 3 Stacking Model
**Construction:** The techniques used to increase accuracy are mainly, bagging, boosting and stacking. In XGBoost it performs gradient boosting, and in this model i have
implemented stacking where we stack multiple models and enhace the accuracy. In XGBoost its a case of boosting, here it is stacking. There it is just one model, whereas here
we use two base learners, XGBoost as well as Random Forest. There is a meta model as well for which i have used ridge. In XGBoost scaling is handled whereas here I let  the scaling
happen internally for XGBoost and none for Random Forest. It harness the capacity of both models. Uses 50 n_estimators of both unlike XGBoost which is of only XGBoost.

**Evaluation:** Like I have said above, it harness the best of both the models and gives much better mean absolute error, root mean squared error and r squared. This implies
that it is good at penalising large errors as well as captures the relationshipand trends very well. This is indicative of high predictive power from the model. 


## Best Model

**Model:** Stacking Model
Despite having a higher Mean Absolute Error than Random Forest, I would say this is the best model due its Lower Root Mean Squared Error and Higher R squared value. It combines
both Random Forest as well as XGBoost and uses Ridge as a meta model and increased the variance that has been explained and to the extent that the complexities of predicting 
time taken have been understood. It captures large errors as well as has better performance.