using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class UserInfo : MonoBehaviour
{
    LoginController login;
    // Start is called before the first frame update
    void Start()
    {
        login = GameObject.Find("LoginController").GetComponent<LoginController>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
