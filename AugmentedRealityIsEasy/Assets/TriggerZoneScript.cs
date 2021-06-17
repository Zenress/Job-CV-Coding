using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TriggerZoneScript : MonoBehaviour
{
    Animation move;
    // Start is called before the first frame update
    void Start()
    {
        move = GetComponent<Animation>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnCollisionEnter(Collision collision)
    {
        if (collision.collider.CompareTag("TriggerAnimation"))
        {
            move.Play();
        }
        else
        {
        }
    }
}
