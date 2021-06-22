using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Firebase.Extensions;
using Firebase.Firestore;

public class TileInstantiation : MonoBehaviour
{
    //Needed for instantiation of the tiles
    [SerializeField]
    internal GameObject tilePrefab;
    internal GameObject instantiatedTile;
    internal List<GameObject> tiles;

    //Needed for GetBookList
    internal List<TileObject> listOfHardware = new List<TileObject>();
    internal bool getHardwareDone = false;
    internal FirebaseFirestore db;
    // Start is called before the first frame update
    void Start()
    {
        //Assigning the correct gameobject and components to the variables
        db = FirebaseFirestore.DefaultInstance;
    }

    //Method for getting the list of tiles
    internal void GetHardwareList()
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
                foreach (KeyValuePair<string, object> pair in books)
                {
                    Debug.Log($"{pair.Key}  {pair.Value}");
                    switch (pair.Key)
                    {
                        case "type":
                            newTile.Type = (string)pair.Value;
                            break;

                        case "navn":
                            newTile.Name = (string)pair.Value;
                            break;

                        case "udlånt":
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
}
