import 'package:flutter/material.dart';

// entry point for the app,
// the => operator is shorthand for {} when there is only one line of code
void main() => runApp(MyApp());

// the root widget of our application
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Container(
          alignment: Alignment.topCenter,
          padding: EdgeInsets.fromLTRB(0, 30, 0, 0),
          child: Stack(
              children: <Widget>[
              Container(
                alignment: Alignment.topCenter,
              child:
                Image.asset(
                'images/aceso-logo-2.png',
                ),
              ),

              Container(
                alignment: Alignment.bottomCenter,
                padding: EdgeInsets.fromLTRB(0, 0, 0, 50),
                child:
                new RaisedButton(
                  onPressed: () {

                  },
                  textColor: Colors.white,
                  color: Colors.blue[700],
                  shape: StadiumBorder(),
                  padding: const EdgeInsets.fromLTRB(40, 20, 40, 20),
                  child: new Text(
                    "START",
                    style: TextStyle(
                      fontSize: 20.0,
                      letterSpacing: 3,
                      fontWeight: FontWeight.w400,
                    ),
                  ),
                  ),
              ),
          ]



          ),
          ),
        ),
      );
  }
}

