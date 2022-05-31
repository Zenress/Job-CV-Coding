using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class CreateCube : MonoBehaviour
{
    [SerializeField] GameObject cube;
    internal GameObject generatedCube;
    internal Vector3[] vectors = new Vector3[] {new Vector3(1,0,0),new Vector3(0,0,1) };
    internal System.Random rand = new System.Random();
    internal List<GameObject> cubes = new List<GameObject>();
    internal Vector3 pos;
    internal Vector3 LastCubePos;
    internal int Index;
    readonly Vector3[] rotation = new Vector3[] {new Vector3(0,90,0), new Vector3(0,0,0) };

    private GameMasterScript _script;
    private ScoreBoardFireStore _database;
    // Start is called before the first frame update
    void Start()
    {
        _script = GameObject.Find("Gamemaster").GetComponent<GameMasterScript>();
        _database = GameObject.Find("Gamemaster").GetComponent<ScoreBoardFireStore>();
        
    }

    // Update is called once per frame
    void Update()
    {
        if (_script.playClicked == true)
        {
            switch (_script.state)
            {
                case 0:

                    break;

                case 1:
                    for (int i = 0; i < 20; i++)
                    {
                        CreateCubes();
                        Debug.Log(cubes[i]);
                    }
                    LastCubePos = pos;
                    Index = 0;
                    _database.score = 0;
                    break;
                case 2:

                    break;

                case 3:

                    break;
            }
            _script.playClicked = false;
        }

    }

    void CreateCubes()
    {        
        pos += vectors[rand.Next(0, 2)];
        generatedCube = GetComponent<GameObject>();
        generatedCube = Instantiate(cube,new Vector3(pos.x, pos.y,pos.z), Quaternion.identity);
        generatedCube.transform.Rotate(rotation[rand.Next(0,2)]);
        cubes.Add(generatedCube);
        pos = generatedCube.transform.position;        
    }

}
