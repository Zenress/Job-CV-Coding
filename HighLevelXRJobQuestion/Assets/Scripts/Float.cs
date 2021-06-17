using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Float : MonoBehaviour
{
    Vector2 floatY;
    float originalY;

    public float floatStrength;

    void Start()
    {
        this.originalY = this.transform.position.y;
    }

    void FixedUpdate()
    {
        floatY = transform.position;
        floatY.y = originalY + (Mathf.Sin(Time.time) * floatStrength);
        transform.position = floatY;
    }
}
