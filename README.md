# Virtual-Paint
Webcam based painting environment. Users can paint virtually over the screen using the markers in their hands. It uses color recognition on the back end, creating a pointer at the tip of the marker and then keeps filling the area with the same color wherever the marker is moved.

You can add a new color by running the finding values file and keeping the color pen in front of the web cam and adjust the trackbars to make everything else black but the color to be detected. From there you will get the values of 6 parameters namely s_min, s_max, h_min, h_max, v_min, v_max.

To add the color you just need to add those 6 values to the myColors list in the virtual paint code file and also find the filling color by finding the rgb values of the color and add it to the myColorValues list in the virtual paint code file.
