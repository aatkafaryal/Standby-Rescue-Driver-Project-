# Standby Rescue Driver Predictor Project
In this data science project a web application is createdto predict the number of satndby rescue drivers needed daily.

1. **Business Problem:**
   The Berlin’s red-cross rescue service provides rescue drivers for emergency situations. Their HR was struggling with the duty plan of standby rescue drivers. They were not able to efficiently estimate the number of standby rescue drivers activated on a given day. Every day a certain number of rescue drivers are on duty. However, due to short-term sickness of rescue drivers or an unusual amount of emergency calls often more drivers are needed than initially expected. Hence, they decided to kept 90 standby drivers "on hold" and activated when needed.But this approach of having a daily fixed number of standbys is not efficient because there are days with too many standbys followed by days with not enough standbys. Therefore, the business aims at a more dynamical standby allocation of standby rescue driver, and most important, the model should minimize dates with not enough standby drivers at hand.
2. **Solution:**
   To solve this problem I developed a Machine learning Model which can efficiently predict number of rescue drivers needed daily. The model was trained using XGBoost regression algorithm with 92% accuracy. Then I created a web application using Flask to use this model for prediction. The project is done by using CRISP-DM approach in following steps:
     1. Business Objective
     2. Data Understanding via EDA
     3. Data Preparation
     4. Model building
     5. Evaluation
     6. Deployment
  
     
