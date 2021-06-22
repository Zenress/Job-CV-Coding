using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class SwipeMenuRightBtnScript : MonoBehaviour
{
    internal Button saveChangesBtn;
    Button signOutBtn;
    // Start is called before the first frame update
    void Start()
    {
        signOutBtn = GameObject.Find("SignOutBtn").GetComponent<Button>();
        saveChangesBtn = GameObject.Find("SaveBtn").GetComponent<Button>();
        signOutBtn.onClick.AddListener(signOut);
    }

    void signOut()
    {
        SceneManager.LoadScene("LoginScreen");
    }
}
