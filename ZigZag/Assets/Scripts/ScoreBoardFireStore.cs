using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using Firebase.Extensions;
using Firebase.Firestore;
using System;
using System.Threading;
using System.Threading.Tasks;

public class ScoreBoardFireStore : MonoBehaviour
{
    [SerializeField] TMP_Text menuScoreBoard;
    [SerializeField] TMP_Text liveScoreBoard;
    internal uint score = 0;
    internal MoveBall moveBall;
    internal int previousHighScore = 0;
    [SerializeField] TMP_InputField text;
    [SerializeField] TMP_Text highscoreText;
    internal GameMasterScript gm;
    private SubmitBtnScript submitBtn;
    internal bool AddingHasRun = false;
    internal bool ScoreboardLoaded = false;
    internal bool GetScoresHasRun = false;
    internal List<KeyValuePair<string, object>> highScores = new List<KeyValuePair<string, object>>();
    private float waitTime = 1.0f;
    private float timer = 0;

    FirebaseFirestore db;
    // Start is called before the first frame update
    void Start()
    {
        db = FirebaseFirestore.DefaultInstance;
        moveBall = GameObject.Find("Sphere").GetComponent<MoveBall>();
        gm = GetComponent<GameMasterScript>();
        submitBtn = GameObject.Find("Submit").GetComponent<SubmitBtnScript>();      
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void FixedUpdate()
    {        
        liveScoreBoard.text = score.ToString();
        if (moveBall.IsDead == true)
        {
            timer += Time.deltaTime;
            gm.state = 3;
            if (GetScoresHasRun == false)
            {
                GetScores();
                
            }
            if (ScoreboardLoaded == false && timer > waitTime)
            {
                PrintHighscores();
            }
            if (AddingHasRun == false)
            {                
                AddHighscore();
            }
        }
    }
    void GetScores()
    {
        Query allCitiesQuery = db.Collection("Scores").OrderByDescending("Score");
        allCitiesQuery.GetSnapshotAsync().ContinueWithOnMainThread(task =>
        {
            QuerySnapshot allCitiesQuerySnapshot = task.Result;
            foreach (DocumentSnapshot documentSnapshot in allCitiesQuerySnapshot.Documents)
            {
                Debug.Log(string.Format("Document data for {0} document:", documentSnapshot.Id));
                Dictionary<string, object> highscores = documentSnapshot.ToDictionary();
                foreach (KeyValuePair<string, object> pair in highscores)
                {
                    Debug.Log(string.Format("{0}: {1}", pair.Key, pair.Value));
                    highScores.Add(pair);
                }
            }            
        });
        
        GetScoresHasRun = true;
    }

    void PrintHighscores()
    {
            highscoreText.text = $"{highScores[0].Value} = {highScores[1].Value} \n" +
            $"{highScores[2].Value} = {highScores[3].Value} \n" +
            $"{highScores[4].Value} = {highScores[5].Value} \n" +
            $"{highScores[6].Value} = {highScores[7].Value} \n" +
            $"{highScores[8].Value} = {highScores[9].Value} \n" +
            $"{highScores[10].Value} = {highScores[11].Value} \n" +
            $"{highScores[12].Value} = {highScores[13].Value} \n" +
            $"{highScores[14].Value} = {highScores[15].Value} \n";
            menuScoreBoard.text = "Score:" + " " + score.ToString();
            ScoreboardLoaded = true;
    }

    void AddHighscore()
    {        
        Debug.Log("Reached the start of Method: AddHighscore");
        if (submitBtn.IsClicked == true)
        {
            Debug.Log("Reached inside the first if statement");
            
            if (uint.Parse(highScores[1].Value.ToString()) < score)
            {
                Dictionary<string, object> createHighScore = new Dictionary<string, object>
                {
                    { "Score", score },
                    { "Name", text.text }
                };
                db.Collection("Scores").AddAsync(createHighScore).ContinueWithOnMainThread(utask => {
                    DocumentReference addedDocRef = utask.Result;
                    Debug.Log(string.Format("Added document with ID: {0}.", addedDocRef.Id));
                });                            
            }
            AddingHasRun = true;
        }

        // Newline to separate entries
        Debug.Log("");            
    }
}
