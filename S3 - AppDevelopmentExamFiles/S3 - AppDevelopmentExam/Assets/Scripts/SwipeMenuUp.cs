using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.UI;

public class SwipeMenuUp : MonoBehaviour
{
    //Creating the right variables so that we can access the right things in the maincontroller gameobject
    internal Transform menuParent;
    internal TMP_InputField navn;
    internal TMP_InputField type;
    internal Toggle udlånt;
    // Start is called before the first frame update
    private void Awake()
    {
        //Assigning the correct gameobject and components to the variables
        menuParent = GetComponent<Transform>();
        navn = GameObject.Find("Navn2(TMP)").GetComponent<TMP_InputField>();
        type = GameObject.Find("Type(TMP)").GetComponent<TMP_InputField>();
        udlånt = GameObject.Find("Udlånt").GetComponent<Toggle>();
    }
}
