using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AndroidControls : MonoBehaviour
{
    private Vector3 fp;   //First touch position
    private Vector3 lp;   //Last touch position
    private float dragDistance;  //minimum distance for a swipe to be registered
    internal bool swipedRight = false;
    internal bool swipedLeft = false;
    internal bool menuIsShown = false;
    internal bool closeMenu = false;

    void Start()
    {
        dragDistance = Screen.width * 5 / 100; //dragDistance is 15% height of the screen
    }

    void Update()
    {
        if (Input.touchCount == 1) // user is touching the screen with a single touch
        {
            Touch touch = Input.GetTouch(0); // get the touch
            if (touch.phase == TouchPhase.Began) //check for the first touch
            {
                fp = touch.position;
                lp = touch.position;
            }
            else if (touch.phase == TouchPhase.Moved) // update the last position based on where they moved
            {
                lp = touch.position;
            }
            else if (touch.phase == TouchPhase.Ended) //check if the finger is removed from the screen
            {
                lp = touch.position;  //last touch position. Ommitted if you use list

                //Check if drag distance is greater than 20% of the screen height
                if (Mathf.Abs(lp.x - fp.x) > dragDistance || Mathf.Abs(lp.y - fp.y) > dragDistance)
                {//It's a drag
                 //check if the drag is vertical or horizontal
                    if (Mathf.Abs(lp.x - fp.x) > Mathf.Abs(lp.y - fp.y))
                    {   //If the horizontal movement is greater than the vertical movement...
                        if ((lp.x > fp.x) && menuIsShown == false)  //If the movement was to the right)
                        {   //Right swipe
                            Debug.Log("Right Swipe");
                            swipedLeft = false;
                            swipedRight = true;
                            menuIsShown = true;
                        }
                        else if (lp.x < fp.x && menuIsShown == true)
                        {
                            swipedRight = false;
                            swipedLeft = true;
                            menuIsShown = false;
                            closeMenu = true;
                        }
                        else
                        {   //Left swipe
                            Debug.Log("Left Swipe");
                            swipedRight = false;
                            swipedLeft = true;
                        }
                    }
                    else
                    {   //the vertical movement is greater than the horizontal movement
                        if (lp.y > fp.y)  //If the movement was up
                        {   //Up swipe
                            Debug.Log("Up Swipe");
                        }
                        else
                        {   //Down swipe
                            Debug.Log("Down Swipe");
                        }
                    }
                }
                else
                {   //It's a tap as the drag distance is less than 20% of the screen height
                    Debug.Log("Tap");
                }
            }
        }
    }
}
