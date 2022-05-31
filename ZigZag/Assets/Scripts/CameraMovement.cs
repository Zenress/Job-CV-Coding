using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraMovement : MonoBehaviour
{
    [SerializeField] Camera cam;
    [SerializeField] GameObject player;
    private Vector3 offset = new Vector3(-5, 5, -5);
    // Start is called before the first frame update
    void Start()
    {
        cam.transform.position = offset + player.transform.position;
    }

    // Update is called once per frame
    void Update()
    {
        if (player != null && cam.transform.position.y > 5.7)
        {
            cam.transform.position = offset + player.transform.position;
        }        
    }
}
