using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameMasterScript : MonoBehaviour
{
    internal enum GameState
    {
        IsMenu,
        IsPlaying,
        IsPaused,
        IsEnded,
    }

    internal int state;
    internal bool playClicked = false;
    private void Awake()
    {
        state = (int)GameState.IsMenu;
    }
}
