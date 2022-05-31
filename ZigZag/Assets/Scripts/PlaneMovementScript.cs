using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlaneMovementScript : MonoBehaviour
{
    // Start is called before the first frame update
    // Scroll main texture based on time

    private float scrollSpeed = 0.05f;
    private Renderer rend;

    void Start()
    {
        rend = GetComponent<Renderer>();
    }

    void Update()
    {
        float offset = Time.time * scrollSpeed;
        rend.material.SetTextureOffset("_MainTex", new Vector2(0.009f, -offset));
    }
}
