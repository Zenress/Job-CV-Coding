using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class SwipeMenuUpBtnScript : MonoBehaviour
{
    //Creating the variables needed in the Maincontroller gameobject
    internal Button createNewBtn;
    // Start is called before the first frame update
    void Start()
    {
        //Assigning the correct gameobject and components to the variables
        createNewBtn = GetComponent<Button>();
    }

}
