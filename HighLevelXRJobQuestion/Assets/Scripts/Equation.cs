using System;
using UnityEngine;

// C# example.
public class Equation : MonoBehaviour
{
    Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
    RaycastHit hit;
    
    //Enum for making the code easier to read. The squares also use the assigned numbers in the switch statement
    enum Squares
    {
        red,
        blue,
        green,
        black
    }
    //This variable is always equal to the square that you hit
    int hitSquare;
    void FixedUpdate()
    {
        //Variables for the layer masks. Used for determining which layers' collider shold be checked
        int redSquare = 1 << 10;
        int blueSquare = 1 << 11;
        int greenSquare = 1 << 12;
        int blackSquare = 1 << 13;

        
        // Does the ray intersect any objects in the color layers?
        //Draws a red line whenever the raycast hits the object with the red layer
        if (Physics.Raycast(transform.position, transform.TransformDirection(Vector3.forward), out hit, Mathf.Infinity, redSquare))
        {
            Debug.DrawLine(ray.origin, hit.point, Color.red);
            Debug.Log("Red Hit");
            hitSquare = (int)Squares.red;
            rotateCube();
        }
        //Draws a blue line whenever the raycast hits the object with the blue layer

        if (Physics.Raycast(transform.position, transform.TransformDirection(Vector3.forward), out hit, Mathf.Infinity, blueSquare))
        {
            Debug.DrawLine(ray.origin, hit.point, Color.blue);
            Debug.Log("Blue Hit");
            hitSquare = (int)Squares.blue;
            rotateCube();
        }
        //Draws a green line whenever the raycast hits the object with the green layer

        if (Physics.Raycast(transform.position, transform.TransformDirection(Vector3.forward), out hit, Mathf.Infinity, greenSquare))
        {
            Debug.DrawLine(ray.origin, hit.point, Color.green);
            Debug.Log("Green Hit");
            hitSquare = (int)Squares.green;
            rotateCube();
        }
        //Draws a black line whenever the raycast hits the object with the black layer
        if (Physics.Raycast(transform.position, transform.TransformDirection(Vector3.forward), out hit, Mathf.Infinity, blackSquare))
        {
            Debug.DrawLine(ray.origin, hit.point, Color.black);
            Debug.Log("Black Hit");
            hitSquare = (int)Squares.black;
            rotateCube();
        }
        //Draws a white ray when ever you move around not aiming at a color square
        else
        {
            Debug.DrawRay(transform.position, transform.TransformDirection(Vector3.forward) * 1000, Color.white);
            Debug.Log("Did not Hit");
        }
    }

    private void Start()
    {
        //Assigning the variables below at the start of the application
        parentCube = GameObject.Find("ParentCube").GetComponent<Transform>();
        blueCube = GameObject.Find("Blue").GetComponent<Transform>();
        greenCube = GameObject.Find("Green").GetComponent<Transform>();
        blackCube = GameObject.Find("Black").GetComponent<Transform>();
        redRun = false;
        blueRun = false;
        greenRun = false;
        blackRun = false;
        startRotation = parentCube.rotation;
    }

    //Variables and fields used for rotating the parent cube. This script is a singleton right now
    Transform parentCube;
    Transform blueCube;
    Transform greenCube;
    Transform blackCube;
    Vector3 rotationDifference;
    Quaternion startRotation;
    int previousTarget;
    bool redRun;
    bool blueRun;
    bool blackRun;
    bool greenRun;

    //Rotatecube method that rotates the cube
    void rotateCube()
    {
        //Switch statement that runs on the variable: hitSquare. That variable is equal to what the raycast was hitting
        switch (hitSquare)
        {
            case 0:
                //If the red cube is hit, it applies this code
                if (redRun == false)
                {
                    parentCube.SetPositionAndRotation(parentCube.position,startRotation);
                    previousTarget = hitSquare;
                    //Making sure the right bools are changed
                    blueRun = false;
                    redRun = true;
                    greenRun = false;
                    blackRun = false;
                }                
                break;
            case 1:
                //If the blue cube is hit, it applies this code
                if (blueRun == false)
                {
                    //There is 2 scenarios. One that it's position is the same as the starting position. Then it runs the code inside the if part
                    if (hit.transform.rotation.eulerAngles.z >= 0)
                    {
                        rotationDifference = hit.transform.rotation.eulerAngles + Quaternion.Inverse(blueCube.rotation).eulerAngles;
                    }
                    //The second scenario is that it has already had it's position changed, therefore this part would be run instead
                    else
                    {
                        rotationDifference = Quaternion.Inverse(hit.transform.rotation).eulerAngles + Quaternion.Inverse(blueCube.rotation).eulerAngles;
                    }
                    //Making sure the right bools are changed
                    blueRun = true;
                    redRun = false;
                    greenRun = false;
                    blackRun = false;
                    parentCube.transform.Rotate(rotationDifference.z, rotationDifference.y, rotationDifference.x);
                    previousTarget = hitSquare;
                }
                break;
            case 2:
                //If the green cube is hit, it applies this code
                if (greenRun == false)
                {
                    //There is 2 scenarios. One that it's position is the same as the black square. Then it runs the code inside the if part
                    if (previousTarget == 3)
                    {
                        parentCube.SetPositionAndRotation(parentCube.position, startRotation);
                        rotationDifference = Quaternion.Inverse(hit.transform.rotation).eulerAngles + Quaternion.Inverse(greenCube.rotation).eulerAngles;
                    }
                    //The second scenario is that it has already had it's position changed or is the starting position, therefore this part would be run instead
                    else if (previousTarget == 1 || previousTarget == 0 || previousTarget == 2)
                    {
                        rotationDifference = Quaternion.Inverse(hit.transform.rotation).eulerAngles + Quaternion.Inverse(greenCube.rotation).eulerAngles;
                    }
                    //Making sure the right bools are changed
                    blueRun = false;
                    redRun = false;
                    greenRun = true;
                    blackRun = false;
                    parentCube.transform.Rotate(rotationDifference.z, rotationDifference.y, rotationDifference.x);
                    previousTarget = hitSquare;
                }
                break;
            case 3:
                //If black red cube is hit, it applies this code
                if (blackRun == false)
                {
                    if (hit.transform.rotation.eulerAngles.z >= 0 )
                    {
                        rotationDifference = hit.transform.rotation.eulerAngles + Quaternion.Inverse(blackCube.rotation).eulerAngles;
                    }
                    else
                    {
                        rotationDifference = Quaternion.Inverse(hit.transform.rotation).eulerAngles + Quaternion.Inverse(blackCube.rotation).eulerAngles;
                    }
                    //Making sure the right bools are changed
                    blackRun = true;
                    redRun = false;
                    blueRun = false;
                    greenRun = false;
                    parentCube.transform.Rotate(rotationDifference.z, rotationDifference.y, rotationDifference.x);
                    previousTarget = hitSquare;
                }
                break;
        }
        
    }
}
