# ACESO

ACESO is a Machine Learning powered Medical Diagnostic App that can detect both Parkinson's and Malaria. 

The App is written in Dart and uses the Flutter Framework along with the Android SDK. It hooks into a Flask REST API on a Microsoft Azure VM Server with exposed ports. The Flask API calls Keras (a machine learning framework) which is able to load `.h5` files which are my trained CNNs for both Malaria and Parkinson's. 

## Installation

- Load the app via Android Studio
- Launch the application.py on Azure and expose port 80
- Test the app

### Mobile App

![our app](https://i.imgur.com/zZQnbZK.png)

### My Collaborators

![my collabs](https://i.imgur.com/OmIQWCC.jpg)

## License

[MIT](https://github.com/andre-fu/aceso/blob/master/LICENSE) © Kuba Wernerowski, Gaurav Ranganath, Andre Fu
