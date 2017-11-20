
# Titanic Survival Visualization
## Introduction 

**In this project, I analyzed the Titanic dataset in order to find the answers of the following questions: What's the difference of the survival situation among different classes? What's the difference of the survival situation between male and female? What's the difference of the survival situation among different age groups? Therefore, the variables of "Survived", "Pclass", "Sex" and "Age" should be used. Since there are somme null values in the age variable, I deleted the instances with null age. I add a variable of count and set the values to be 1. I changed the variable name of survived to survival and replace the values from 1 and 0 to survived and deceased. I add a new variable of age and assign it to children if the age is less than 19, assign it to adults if the age is between 19 and 64, and assign it to seniors if the age is higher than 65. I change the classifications of class to upper class, middle class and lower class. The dataset is also split based on age.**

## Design

**In order to do the comparisons, I create three buttons for the age groups. People will see the survival situations among different age groups when they press the buttons of Children (1-9),Teenagers (10-18), Adults (19-64) and  Seniors (65+) in both count and percentage ways. For charts within each age group, I divided them into male and female. For each gender, the survival is shown based on different ticket classes. The survived and deceased count is shown by stack with red and blue colors. For x axis, the label is Sex/Ticket Class, which means for each sex (male or female), it's divided into three ticket classes which are lower class, middle class and upper class. For y axis, the labels are count and percentage, which show the survival/deceased in the two ways of count number and ratio. Therefore, the readers can see how the survival situations differ among different age group, sex and ticket classes.**

## Feedback

**provider 1:the Pclass label is kind of confused. The range of y axis is changed based on the data, which actually makes it difficult to comparison.  
Therefore, I changed Pclass into Ticket Class and set the overrideMax of y to 200.   
provider 2: Some survived are on top of the deceased while some deceased are on top of the survived in the bars.   
In new design, I set the order to unify them.   
Provider 3: The setStoryboard function in Dimple is used in the first design, but it's not easy to see the details. The reading speed and focus area varies among different people.  
Therefore, I abadon the use of setStoryboard, instead, I made a button group of the three age group, so the readers can control the visualization by themselves.**

## Summary
 
**As we can see from the charts, most passengers are adults. For  children, children in higher ticket classes have higher survivor rate, however, girls in middle class are 100% survived. For teenagers, all teenagers in middle and upper classes are survived. For adults, male has much lower survivor rate compared with female. The survivor rate for male in second class is relatively lower. The survivor rate of female in upper and middle classes is very high. For the seniors, the survivor rate of male are similar and all of them are extremely low. All senior females survived. In general, females are more likely to survive compared with males. People in higher ticket classes are more likely to survive compared with people in lower ticket classes.**
 


```python

```
