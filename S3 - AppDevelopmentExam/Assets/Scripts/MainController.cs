using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using Firebase.Firestore;
using Firebase.Extensions;
using Firebase.Auth;

public class MainController : MonoBehaviour
{
    //Needed for swipe menues
    AndroidControls aControls;
    SwipeMenu swipeRightControls;
    
    
    //Needed for GetBookList
    List<TileObject> listOfHardware = new List<TileObject>();
    bool getHardwareDone = false;

    //Needed for instatiation
    TileInstantiation tileScript;
    [SerializeField]
    GameObject contentEmpty;
    FirebaseFirestore db;
    List<GameObject> tileList = new List<GameObject>();
    bool hasBeenCalled = false;

    //Needed for controlling login
    LoginController _login;
    private void Awake()
    {
        db = FirebaseFirestore.DefaultInstance;
        GetBookList();
        aControls = GameObject.Find("EventSystem").GetComponent<AndroidControls>();
        swipeRightControls = GameObject.FindGameObjectWithTag("MenuController").GetComponent<SwipeMenu>();
        _login = GameObject.Find("LoginController").GetComponent<LoginController>();
    }

    void Start()
    {        
        tileScript = GetComponent<TileInstantiation>();
        AssignUserProfile();
    }

    // Update is called once per frame
    void Update()
    {
        if (getHardwareDone == true && hasBeenCalled == false)
        {
            InstantiateTiles();
            hasBeenCalled = true;
        }
        if (aControls.swipedRight == true && aControls.closeMenu == false)
        {
            swipeRightControls.menuParent.transform.localPosition = new Vector3(0f, 0f, 0f);
            aControls.swipedRight = false;
        }
        if (aControls.swipedLeft == true && aControls.closeMenu == true)
        {
            swipeRightControls.menuParent.transform.localPosition = new Vector3(-1178f, 0f, 0f);
            aControls.swipedLeft = false;
            aControls.closeMenu = false;
        }
    }

    void GetBookList()
    {
        Query hardwareList = db.Collection("HardwareList");
        hardwareList.GetSnapshotAsync().ContinueWithOnMainThread(task =>
        {
            QuerySnapshot getHardwareList = task.Result;
            foreach (DocumentSnapshot documentSnapshot in getHardwareList.Documents)
            {
                TileObject newTile = new TileObject();
                Debug.Log(string.Format("Document data for {0} document:", documentSnapshot.Id));
                Dictionary<string, object> books = documentSnapshot.ToDictionary();
                foreach (KeyValuePair<string,object> pair in books)
                {
                    Debug.Log($"{pair.Key}  {pair.Value}");
                    switch (pair.Key)
                    {
                        case "type":
                            newTile.Type = (string)pair.Value;
                            break;

                        case "name":
                            newTile.Name = (string)pair.Value;
                            break;

                        case "status":
                            newTile.Status = (bool)pair.Value;
                            break; 

                        case "dato":
                            newTile.DateOfChange = (Timestamp)pair.Value;
                            break;

                        case "id":
                            newTile.Id = (string)pair.Value;
                            break;
                    }
                }
                listOfHardware.Add(newTile);
                foreach (TileObject item in listOfHardware)
                {
                    Debug.Log(item.Id);
                    Debug.Log(item.Type);
                    Debug.Log(item.Name);
                    Debug.Log(item.Status);
                    Debug.Log(item.DateOfChange);
                }
                Debug.Log(listOfHardware.Count);
                getHardwareDone = true;
            }
        });
    }

    void InstantiateTiles()
    {
        for (int i = 0; i < listOfHardware.Count; i++)
        {
            tileScript.instantiatedTile = Instantiate(tileScript.tilePrefab, new Vector3(0,0,0), Quaternion.Euler(0,0,90));
            tileScript.instantiatedTile.transform.SetParent(contentEmpty.transform);
            tileScript.instantiatedTile.transform.localScale = new Vector3(1,1,1);
            tileScript.instantiatedTile.transform.Find("HardwareTileName").GetComponent<TMP_Text>().text = listOfHardware[i].Name;
            tileScript.instantiatedTile.transform.Find("HardwareTileType").GetComponent<TMP_Text>().text = "Type: " + listOfHardware[i].Type;
            tileScript.instantiatedTile.transform.Find("HardwareTileStatus").GetComponent<TMP_Text>().text = "Status: " + listOfHardware[i].Status;
            tileScript.instantiatedTile.transform.Find("HardwareTilesDateOfChange").GetComponent<TMP_Text>().text = "Dato: " + listOfHardware[i].DateOfChange.ToDateTime();
            tileScript.instantiatedTile.SetActive(true);
            tileList.Add(tileScript.instantiatedTile);
            Debug.Log("Instantiated a tile");
        }
    }

    void AssignUserProfile()
    {
        /*FirebaseUser user = auth.CurrentUser;
        if (user != null)
        {
            string name = user.DisplayName;
            string email = user.Email;
            string uid = user.UserId;
            DocumentReference docRef = db.Collection("Brugere").Document(email);
            docRef.GetSnapshotAsync().ContinueWithOnMainThread(task =>
            {
                DocumentSnapshot snapshot = task.Result;
                if (snapshot.Exists)
                {
                    Debug.Log(string.Format("Document data for {0} document:", snapshot.Id));
                    Dictionary<string, object> brugere = snapshot.ToDictionary();
                    foreach (KeyValuePair<string, object> pair in brugere)
                    {
                        Debug.Log(string.Format("{0}: {1}", pair.Key, pair.Value));
                        switch (pair.Key)
                        {
                            case "email":
                                swipeRightControls.email.text = (string)pair.Value;
                                break;
                            case "navn":
                                swipeRightControls.navn.text = (string)pair.Value;
                                break;
                            case "mobilnummer":
                                swipeRightControls.phonenumber.text = (string)pair.Value;
                                break;
                            case "fødselsdag":
                                swipeRightControls.birthday.text = (string)pair.Value;
                                break;
                            case "adresse":
                                swipeRightControls.adresse.text = (string)pair.Value;
                                break;
                        }
                    }
                }
                else
                {
                    Debug.Log(string.Format("Document {0} does not exist!", snapshot.Id));
                }
            });
        }*/
    }

    void SaveUserProfile()
    {
        /*DocumentReference docRef = db.Collection("Brugere").Document(email);
        Dictionary<string, object> bruger = new Dictionary<string, object>
            {
                    { "email", email },
                    { "navn", swipeRightControls.navn.text },
                    { "adresse", swipeRightControls.adresse.text },
                    { "mobilnummer",swipeRightControls.phonenumber.text },
                    { "fødselsdag",swipeRightControls.birthday.text }
            };
        docRef.SetAsync(bruger).ContinueWithOnMainThread(task => {
            Debug.Log("Added data to the LA document in the cities collection.");
        });*/
    }
}

public class TileObject
{
    private string id;
    private string name;
    private string type;
    private bool status;
    private Timestamp dateOfChange;
    public string Id { get { return id; } set { id = value; } }
    public string Name { get { return name; } set { name = value; } }
    public string Type { get { return type; } set { type = value; } }
    public bool Status { get { return status; } set { status = value; } }
    public Timestamp DateOfChange { get { return dateOfChange; } set { dateOfChange = value; } }
}
