using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ButttonScript : MonoBehaviour
{
    private GameMasterScript _script;
    private Button playBtn;
    private Canvas mainMenu;
    private Canvas gameMenu;
    private Canvas pauseMenu;
    private Canvas scoreboardMenu;
    private ScoreBoardFireStore _scoreBoard;
    // Start is called before the first frame update
    void Start()
    {
        _script = GameObject.Find("Gamemaster").GetComponent<GameMasterScript>();
        mainMenu = GetComponentInParent<Canvas>();
        gameMenu = GameObject.Find("GameMenu").GetComponent<Canvas>();
        pauseMenu = GameObject.Find("PauseMenu").GetComponent<Canvas>();
        scoreboardMenu = GameObject.Find("ScoreBoardMenu").GetComponent<Canvas>();
        playBtn = GetComponent<Button>();
        playBtn.onClick.AddListener(OnPlayBtnClick);
        pauseMenu.enabled = false;
        scoreboardMenu.enabled = false;
        gameMenu.enabled = false;
        mainMenu.enabled = true;
        _script.state = 0;
        _scoreBoard = GameObject.Find("Gamemaster").GetComponent<ScoreBoardFireStore>();
    }

    // Update is called once per frame
    void Update()
    {
        switch (_script.state)
        {
            case 0:

                break;

            case 1:
                
                break;
            case 2:

                break;

            case 3:
                gameMenu.enabled = false;
                scoreboardMenu.enabled = true;
                break;
        }
    }

    void OnPlayBtnClick()
    {
        if (_script.state == 0)
        {
            _script.state = 1;
            mainMenu.enabled = false;
            gameMenu.enabled = true;
            _script.playClicked = true;
            _scoreBoard.AddingHasRun = false;
        }
    }
}
