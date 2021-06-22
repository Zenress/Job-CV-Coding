using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class SwipeMenu : MonoBehaviour
{
    //Making the neccesary variables so that we can acces the right things in the maincontroller gameobject
    internal Transform menuParent;
    internal TMP_InputField navn;
    internal TMP_InputField email;
    internal TMP_InputField phonenumber;
    internal TMP_InputField adresse;
    internal TMP_InputField birthday;
    // Start is called before the first frame update
    private void Awake()
    {
        menuParent = GetComponent<Transform>();
        navn = GameObject.Find("Navn(TMP)").GetComponent<TMP_InputField>();
        email = GameObject.Find("Email(TMP)").GetComponent<TMP_InputField>();
        phonenumber = GameObject.Find("Mobilnummer(TMP)").GetComponent<TMP_InputField>();
        adresse = GameObject.Find("Adresse(TMP)").GetComponent<TMP_InputField>();
        birthday = GameObject.Find("Fødselsdag(TMP)").GetComponent<TMP_InputField>();
    }
}
