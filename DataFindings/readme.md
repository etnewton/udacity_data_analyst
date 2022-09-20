# Diamonds Data Exploration

## Dataset

The data is provided by Prosper for 113,937 loans. This data set contains 81 variables about each loan. This data can be obtained from [here] (https://s3.amazonaws.com/udacity-hosted-downloads/ud651/prosperLoanData.csv). With additional information about definitions of the features defined [here] (https://docs.google.com/spreadsheets/d/1gDyi_L4UvIrLTEC6Wri5nbaMmkGmLQBk-Yx3z0XDEtI/edit#gid=0).

## Summary of Findings

In my exploration I found positive relationships with borrower's APR/rate and estimated loss/return. Also found negative relationship between original loan amount and estimated loss. When we looked at the distribution for the logarithmic original loan amount we so a multimodal distribution of the loan amount with peaks at 5k intervals. We additionally saw that the prosper score was roughly normally distributed in the data with a mean around 5.

Outside of the main features we focused on we so that after doing a logarithmic scale transform on the investors data that there was a large amount of loans with only a single investor however it was then normally distribution with the mean roughly around 100 after excluding the loans with only a single investor. Additionally around investors for a given loan that the higher number of investors were associated with a lower estimated loss on the loan.

## Key Insights for Presentation

On the presentation I focused on show the relationships around original loan price to the features of estimated loss and prosper score and then looked at how those feature differed across the categorical features of occupation type and loan status.

Once I introduced the occupation status I pointed out how the professional occupation was associated with higher loan amounts and lower estimaed loss, where as unskilled labor and students had the lowest loan amounts and highest loss. Then I looked at how the how loan amount with prosper score differed when looking at the 3 loan status of completed, defaulted, and charged off and futher breaking those out to show the occupation types again point out how the professional types showed more favorable aspects in teams of higher loan amounts being completed and lower estimated loss.