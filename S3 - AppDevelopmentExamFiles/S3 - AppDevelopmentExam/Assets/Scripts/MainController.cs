using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using Firebase.Firestore;
using Firebase.Extensions;
using Firebase.Auth;
using UnityEngine.SceneManagement;

public class MainController : MonoBehaviour
{
    //Needed for swipe right Menu
    AndroidControls aControls;
    SwipeMenu swipeRightControls;

    //Needed for CrudBtn
    CRUDBtnScript crudBtn1;
    CRUDBtnScript crudBtn2;
    SwipeMenuUp swipeUpControls;
    bool menuOpen;

    //Needed for CreateNewBtn
    SwipeMenuUpBtnScript swipeUpBtn;

    //Needed for saveUserProfile
    SwipeMenuRightBtnScript swipeRightBtn;

    //Needed for instatiation
    TileInstantiation tileScript;
    [SerializeField]
    GameObject contentEmpty;
    FirebaseFirestore db;
    List<GameObject> tileList = new List<GameObject>();
    bool hasBeenCalled = false;

    //Used for holding the currently signed in users email
    string userEmail = "";
    private void Awake()
    {
        //For Tileinstantiation
        tileScript = GetComponent<TileInstantiation>();        
        //For SwipeRightMenu
        aControls = GameObject.Find("EventSystem").GetComponent<AndroidControls>();
        swipeRightControls = GameObject.FindGameObjectWithTag("MenuController").GetComponent<SwipeMenu>();
        swipeRightBtn = GameObject.Find("Buttons(Empty)").GetComponent<SwipeMenuRightBtnScript>();
        userEmail = PlayerPrefs.GetString("userEmail");
        //For SwipeUpMenu
        crudBtn1 = GameObject.FindGameObjectWithTag("CrudBtn1").GetComponent<CRUDBtnScript>();
        crudBtn2 = GameObject.FindGameObjectWithTag("CrudBtn2").GetComponent<CRUDBtnScript>();
        swipeUpControls = GameObject.Find("SwipeMenuUp").GetComponent<SwipeMenuUp>();
        swipeUpBtn = GameObject.Find("LavNyBtn").GetComponent<SwipeMenuUpBtnScript>();

        db = FirebaseFirestore.DefaultInstance;
    }

    void Start()
    {
        //Assigning and running the needed methods to get everything up and running
        menuOpen = false;
        tileScript.GetHardwareList();
        AssignUserProfile();
        swipeRightBtn.saveChangesBtn.onClick.AddListener(SaveUserProfile);
        crudBtn1.crudBtn.onClick.AddListener(MoveCRUDMenu);
        crudBtn2.crudBtn.onClick.AddListener(MoveCRUDMenu);
        swipeUpBtn.createNewBtn.onClick.AddListener(CreateItem);
    }

    // Update is called once per frame
    void Update()
    {
        //Making sure that we have the hardwarelist before initializing a tile
        if (tileScript.getHardwareDone == true && hasBeenCalled == false)
        {
            InstantiateTiles();
            hasBeenCalled = true;
        }
        //Checking if the swipe menu is out or not and then acting accordingly
        if (aControls.swipedRight == true && aControls.closeMenu == false)
        {
            swipeRightControls.menuParent.transform.localPosition = new Vector3(0f, 0f, 0f);
            aControls.swipedRight = false;
        }
        //Checking if the swipe menu is out or not and then acting accordingly
        if (aControls.swipedLeft == true && aControls.closeMenu == true)
        {
            swipeRightControls.menuParent.transform.localPosition = new Vector3(-1178f, 0f, 0f);
            aControls.swipedLeft = false;
            aControls.closeMenu = false;
        }
    }

    //Method for creating an item with the input fields in the swipe up menu
    void CreateItem()
    {        
        DocumentReference docRef = db.Collection("HardwareList").Document(swipeUpControls.navn.text);
        Dictionary<string, object> hardware = new Dictionary<string, object>
            {
                    { "navn", swipeUpControls.navn.text},
                    { "type", swipeUpControls.type.text},
                    { "udlånt", swipeUpControls.udlånt.isOn},
                    {   "dato", Timestamp.GetCurrentTimestamp() },
            };
        docRef.SetAsync(hardware).ContinueWithOnMainThread(task => {
            Debug.Log("Added data to the LA document in the HardwareList collection.");
        });
        SceneManager.LoadScene("MainContentScreen");
    }

    #region CRUDMenu
    //Moving the swipe up menu
    void MoveCRUDMenu()
    {
        if (menuOpen == false)
        {
            swipeUpControls.menuParent.transform.localPosition = new Vector3(-1178f, 2576f, 0f);
            menuOpen = true;
        }
        else if (menuOpen == true)
        {
            swipeUpControls.menuParent.transform.localPosition = new Vector3(-1178f, 0f, 0f);
            menuOpen = false;
        }
        
    }
    #endregion
    #region Tile instantiation
    //The method for instantiating the tile prefab, and making it fit accordinlgy to the screen size
    void InstantiateTiles()
    {
        for (int i = 0; i < tileScript.listOfHardware.Count; i++)
        {
            tileScript.instantiatedTile = Instantiate(tileScript.tilePrefab, new Vector3(0,0,0), Quaternion.Euler(0,0,90));
            tileScript.instantiatedTile.transform.SetParent(contentEmpty.transform);
            tileScript.instantiatedTile.transform.localScale = new Vector3(1,1,1);
            tileScript.instantiatedTile.transform.Find("HardwareTileName").GetComponent<TMP_Text>().text = tileScript.listOfHardware[i].Name;
            tileScript.instantiatedTile.transform.Find("HardwareTileType").GetComponent<TMP_Text>().text = "Type: " + tileScript.listOfHardware[i].Type;
            tileScript.instantiatedTile.transform.Find("HardwareTileStatus").GetComponent<TMP_Text>().text = "Udlånt: " + tileScript.listOfHardware[i].Status;
            tileScript.instantiatedTile.transform.Find("HardwareTilesDateOfChange").GetComponent<TMP_Text>().text = "Dato: " + tileScript.listOfHardware[i].DateOfChange.ToDateTime();
            tileScript.instantiatedTile.SetActive(true);
            tileList.Add(tileScript.instantiatedTile);
            Debug.Log("Instantiated a tile");
        }
    }
    #endregion
    #region User Profile
    //Assigning the input fields on the swipe right menu with the information available, as to let the user know what is left and need to be typed
    void AssignUserProfile()
    {
        if (userEmail != null)
        {
            DocumentReference docRef = db.Collection("Brugere").Document(userEmail);
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
        }

    }

    //For the save button that saves what the user has edited
    void SaveUserProfile()
    {
        DocumentReference docRef = db.Collection("Brugere").Document(userEmail);
        Dictionary<string, object> bruger = new Dictionary<string, object>
            {
                    { "email", userEmail },
                    { "navn", swipeRightControls.navn.text },
                    { "adresse", swipeRightControls.adresse.text },
                    { "mobilnummer",swipeRightControls.phonenumber.text },
                    { "fødselsdag",swipeRightControls.birthday.text }
            };
        docRef.SetAsync(bruger).ContinueWithOnMainThread(task => {
            Debug.Log("Added data to the LA document in the cities collection.");
        });
    }
    #endregion
}

//TileObject for initializing the tiles
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
