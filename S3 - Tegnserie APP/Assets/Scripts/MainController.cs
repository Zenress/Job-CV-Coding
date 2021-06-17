using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using Firebase.Firestore;
using Firebase.Extensions;

public class MainController : MonoBehaviour
{
    TileBtnScript btnScript;

    //Needed for GetBookList
    List<TileObject> listOfBooks = new List<TileObject>();
    bool getBooksDone = false;

    //Needed for instatiation
    TileInstantiation tileScript;
    [SerializeField]
    GameObject contentEmpty;
    FirebaseFirestore db;
    List<GameObject> tileList = new List<GameObject>();
    bool hasBeenCalled = false;
    private void Awake()
    {
        db = FirebaseFirestore.DefaultInstance;
        GetBookList();
    }

    void Start()
    {        
        tileScript = GetComponent<TileInstantiation>();
        /*btnScript = GameObject.Find("BookListAddBtn").GetComponent<TileBtnScript>();*/
    }

    // Update is called once per frame
    void Update()
    {
        if (getBooksDone == true && hasBeenCalled == false)
        {
            InstantiateTiles();
            hasBeenCalled = true;
        }
    }

    void GetBookList()
    {
        Query bookList = db.Collection("BooksList");
        bookList.GetSnapshotAsync().ContinueWithOnMainThread(task =>
        {
            QuerySnapshot getBookList = task.Result;
            foreach (DocumentSnapshot documentSnapshot in getBookList.Documents)
            {
                TileObject newTile = new TileObject();
                Debug.Log(string.Format("Document data for {0} document:", documentSnapshot.Id));
                Dictionary<string, object> books = documentSnapshot.ToDictionary();
                foreach (KeyValuePair<string,object> pair in books)
                {
                    Debug.Log($"{pair.Key}  {pair.Value}");
                    switch (pair.Key)
                    {
                        case "author":
                            newTile.Author = (string)pair.Value;
                            break;

                        case "name":
                            newTile.Name = (string)pair.Value;
                            break;

                        case "genre":
                            newTile.Genre = (string)pair.Value;
                            break; 

                        case "pages":
                            newTile.Pages = (string)pair.Value;
                            break;

                        case "id":
                            newTile.Id = (string)pair.Value;
                            break;
                    }
                }
                listOfBooks.Add(newTile);
                foreach (TileObject item in listOfBooks)
                {
                    Debug.Log(item.Id);
                    Debug.Log(item.Author);
                    Debug.Log(item.Name);
                    Debug.Log(item.Genre);
                    Debug.Log(item.Pages);
                }
                Debug.Log(listOfBooks.Count);
                // Newline to separate entries
                getBooksDone = true;
            }
        });
    }

    void InstantiateTiles()
    {
        for (int i = 0; i < listOfBooks.Count; i++)
        {
            tileScript.instantiatedTile = Instantiate(tileScript.tilePrefab, new Vector3(0,0,0), Quaternion.Euler(0,0,0));
            tileScript.instantiatedTile.transform.Find("BookName").GetComponent<TMP_Text>().text = "Placeholder text";
            tileScript.instantiatedTile.transform.SetParent(contentEmpty.transform);
            tileScript.instantiatedTile.transform.localScale = new Vector3(1,1,1);
            tileScript.instantiatedTile.transform.Find("BookName").GetComponent<TMP_Text>().text = listOfBooks[i].Name;
            tileScript.instantiatedTile.transform.Find("BookAuthor").GetComponent<TMP_Text>().text = "Author: " + listOfBooks[i].Author;
            tileScript.instantiatedTile.transform.Find("BookGenres").GetComponent<TMP_Text>().text = "Genre: " + listOfBooks[i].Genre;
            tileScript.instantiatedTile.transform.Find("BookPages").GetComponent<TMP_Text>().text = "Pages: " + listOfBooks[i].Pages;
            tileList.Add(tileScript.instantiatedTile);
            Debug.Log("Instantiated a tile");
        }
    }
}

public class TileObject
{
    private string id;
    private string name;
    private string author;
    private string genre;
    private string pages;
    public string Id { get { return id; } set { id = value; } }
    public string Name { get { return name; } set { name = value; } }
    public string Author { get { return author; } set { author = value; } }
    public string Genre { get { return genre; } set { genre = value; } }
    public string Pages { get { return pages; } set { pages = value; } }
}
