using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveCube : MonoBehaviour
{
    private CreateCube _script;
    private Vector3 position;
    private ScoreBoardFireStore _database;
    
    // Start is called before the first frame update
    void Start()
    {
        _script = GameObject.Find("Gamemaster").GetComponent<CreateCube>();
        _database = GameObject.Find("Gamemaster").GetComponent<ScoreBoardFireStore>();
        position = _script.LastCubePos;
        _script.pos = position;
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnCollisionExit(Collision collision)
    {
            if (collision.collider.CompareTag("Player"))
            {                
                MoveCubes();
                _database.score += 1;
            }
    }

    void MoveCubes()
    {
        _script.pos += _script.vectors[_script.rand.Next(0, 2)];
        position = _script.pos;
        _script.cubes[_script.Index].transform.position = _script.pos;
        if (_script.Index >= 19)
        {
            _script.Index = 0;
        }
        else
        {
            _script.Index += 1;
        }
        Debug.Log(_script.Index);
    }
}
