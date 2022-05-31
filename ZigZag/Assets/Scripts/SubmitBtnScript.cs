using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class SubmitBtnScript : MonoBehaviour
{
    private GameMasterScript _script;
    private Button submitBtn;
    internal bool IsClicked = false;

    // Start is called before the first frame update
    void Start()
    {
        _script = GameObject.Find("Gamemaster").GetComponent<GameMasterScript>();
        submitBtn = GetComponent<Button>();
        submitBtn.onClick.AddListener(OnSubmitBtnClick);
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void OnSubmitBtnClick()
    {
        if (_script.state == 3)
        {
            IsClicked = true;
        }
    }
}
