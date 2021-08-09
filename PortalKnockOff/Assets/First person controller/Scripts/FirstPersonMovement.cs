using System.Collections.Generic;
using UnityEngine;
using Mirror;

public class FirstPersonMovement : NetworkBehaviour
{
    public float speed = 5;
    Vector2 velocity;

    [Header("Running")]
    public bool canRun = true;
    public bool IsRunning { get; private set; }
    public float runSpeed = 9;
    public KeyCode runningKey = KeyCode.LeftShift;
    /// <summary> Functions to override movement speed. Will use the last added override. </summary>
    public List<System.Func<float>> speedOverrides = new List<System.Func<float>>();

 /*   public override void OnStartLocalPlayer()
    {
        Camera.main.transform.SetParent(transform);
        Camera.main.transform.localPosition = new Vector3(0, 0, 0);
    }*/

    void FixedUpdate()
    {
        if (!isLocalPlayer) { return; }
        // Move.
        IsRunning = canRun && Input.GetKey(runningKey);
        float movingSpeed = IsRunning ? runSpeed : speed;
        if (speedOverrides.Count > 0)
            movingSpeed = speedOverrides[speedOverrides.Count - 1]();
        velocity.y = Input.GetAxis("Vertical") * movingSpeed * Time.deltaTime;
        velocity.x = Input.GetAxis("Horizontal") * movingSpeed * Time.deltaTime;
        transform.Translate(velocity.x, 0, velocity.y);
    }
}