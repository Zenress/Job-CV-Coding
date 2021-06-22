using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using Firebase;
using Firebase.Auth;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
using Firebase.Firestore;
using Firebase.Extensions;

public class LoginController : MonoBehaviour
{
    //Inputfields for email and password
    [SerializeField]
    TMP_InputField email;
    [SerializeField]
    TMP_InputField password;

    //Sign in and sign up buttons
    Button signIn;
    Button signUp;

    public FirebaseAuth auth;
    FirebaseFirestore db;
    bool hasRun = false;
    private void Awake()
    {
        auth = FirebaseAuth.DefaultInstance;
        db = FirebaseFirestore.DefaultInstance;
    }

    void Start()
    {
        //Assigning the correct component to the variables
        signIn = GameObject.Find("SignIn(TMP)").GetComponent<Button>();
        signUp = GameObject.Find("SignUp(TMP)").GetComponent<Button>();
        //Adding action listeners to the buttons
        signIn.onClick.AddListener(Signin);
        signUp.onClick.AddListener(Signup);
        
    }

    private void FixedUpdate()
    {
        if (hasRun == true)
        {
            SceneManager.LoadScene("MainContentScreen");
        }
    }

    //The method for signing in
    void Signin()
    {
        //Authentication method goes here
        auth.SignInWithEmailAndPasswordAsync(email.text, password.text).ContinueWith(task => {
            if (task.IsCanceled)
            {
                Debug.LogError("SignInWithEmailAndPasswordAsync was canceled.");
                return;
            }
            if (task.IsFaulted)
            {
                Debug.LogError("SignInWithEmailAndPasswordAsync encountered an error: " + task.Exception);
                return;
            }

            FirebaseUser newUser = task.Result;
            Debug.LogFormat("User signed in successfully: {0} ({1})",
                newUser.DisplayName, newUser.UserId);
            hasRun = true;
        });        
    }

    //The method for signing up
    void Signup()
    {
        auth.CreateUserWithEmailAndPasswordAsync(email.text, password.text).ContinueWith(task => {
            if (task.IsCanceled)
            {
                Debug.LogError("CreateUserWithEmailAndPasswordAsync was canceled.");
                return;
            }
            if (task.IsFaulted)
            {
                Debug.LogError("CreateUserWithEmailAndPasswordAsync encountered an error: " + task.Exception);
                return;
            }

            // Firebase user has been created.
            FirebaseUser newUser = task.Result;
            Debug.LogFormat("Firebase user created successfully: {0} ({1})",
                newUser.DisplayName, newUser.UserId);
            email.text = "";
            password.text = "";
        });
        DocumentReference docRef = db.Collection("Brugere").Document(email.text);
        Dictionary<string, object> bruger = new Dictionary<string, object>
        {
                { "email", email.text },
        };
        docRef.SetAsync(bruger).ContinueWithOnMainThread(task => {
            Debug.Log("Added data to the LA document in the cities collection.");
        });
    }
}
