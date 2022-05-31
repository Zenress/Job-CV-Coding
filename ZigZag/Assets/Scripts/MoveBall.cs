using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class MoveBall : MonoBehaviour
{
    private Rigidbody rb;
    [SerializeField] GameObject player;
    private bool IsLeft = false;
    internal bool IsDead = false;
    private GameMasterScript _script;
    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();
        _script = GameObject.Find("Gamemaster").GetComponent<GameMasterScript>();
    }

    // Update is called once per frame
    void Update()
    {
        switch (_script.state)
        {
            case 0:
                
                break;

            case 1:
                if (Input.GetMouseButtonDown(0))
                {
                    if (IsLeft == false)
                    {
                        rb.velocity = Vector3.zero;
                        rb.angularVelocity = Vector3.zero;
                        Debug.Log("Works");
                        rb.velocity = new Vector3(0, 0, 2);
                        IsLeft = true;
                    }
                    else
                    {
                        rb.velocity = Vector3.zero;
                        rb.angularVelocity = Vector3.zero;
                        Debug.Log("Doesn't Works");
                        rb.velocity = new Vector3(2, 0, 0);
                        IsLeft = false;
                    }
                }
                if (player.activeSelf == true)
                {
                    if (player.transform.position.y < 0.6)
                    {
                        IsDead = true;
                        Destroy(player, 1);
                        Debug.Log("Died");
                    }
                }
                break;

            case 2:

                break;

            case 3:

                break;
        }
               
    }    
}
