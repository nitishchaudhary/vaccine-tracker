# vaccine-tracker
A simple vaccine finder app

Uses Html Css for frontend formatting and layout.
Flask framework is used for backend functioning along with little bit of javascript.

You can enter your area pincode to get the name and address of availble vaccination slots. It tell you if no slots are available.

Uses the api-setu for fetching the vaccine slots details. Also integrated google maps to show the vaccine locations on the map.(Currently not working as google maps require 
paid account to enable these features)

The app is containerized using docker and the image is pushed to docker hub.(nitishchaudhary/vaccinetracker)
