using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlaneFollowMovement : MonoBehaviour
{
    [SerializeField] GameObject cube;
    [SerializeField] GameObject player;
    // Start is called before the first frame update
    void Start()
    {
        cube.transform.position = new Vector3(0, (float)0.25, 0);
    }

    // Update is called once per frame
    void Update()
    {
        if (player != null && cube.transform.position.y > 0.20 )
        {
            cube.transform.position = player.transform.position - new Vector3(0, (float)0.5, 0);
        }
        
    }
}
