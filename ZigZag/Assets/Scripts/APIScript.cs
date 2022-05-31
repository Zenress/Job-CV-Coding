using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using System.Net;
using Newtonsoft.Json;

public class APIScript : MonoBehaviour
{
    private string weatherType;
    private bool failed;
    private string URL;
    private Material m_Material;
    private void Awake()
    {
        GetWheater();
    }

    void Start()
    {
        m_Material = GetComponent<Renderer>().material;
        if (weatherType != "" && weatherType != null)
        {
            switch (weatherType)
            {
                case "Clear":
                    m_Material.color = Color.blue;
                        break;
            }
        }
    }

    // Update is called once per frame
    void Update()
    {

    }

    //Variables to keep track of city, temperature and if the method has failed
    
    //GetWheater function used to get the current wheater temperature
    public void GetWheater()
    {
        try
        {
            //Getting the textinput and adding it to a variable, afterwards we assign the URL to the variable called URL
            URL = string.Format($"http://api.openweathermap.org/data/2.5/weather?q=Roskilde&units=metric&appid=8ce4b97528c5e39547a6d10a919c79d0");
            weatherType = "";
            //We then make a webrequest instance with the URL variable, afterwards we make sure that the request object knows that it's a get method object
            WebRequest requestObjGet = WebRequest.Create(URL);
            requestObjGet.Method = "GET";
            //We then make a response object that has the unassigned value of null, and then we make the RequestObj's response, the value of the response obj
            HttpWebResponse responseObjGet = null;
            responseObjGet = (HttpWebResponse)requestObjGet.GetResponse();

            //Then we make a new variable, a string that contains the json format result of the API.
            string jsonResult = null;
            //Using a Using argument to read the response stream of the response object
            using (Stream stream = responseObjGet.GetResponseStream())
            {
                //Making an instance of the Streamreader class
                StreamReader sr = new StreamReader(stream);
                //Making the jsonresult variable contain the streamreaders stream. And then closing the streamreader
                jsonResult = sr.ReadToEnd();
                sr.Close();
            }
            //Making the public temperature variable contain the jsonResult variable's value
            Weather[] deserializedClass = JsonConvert.DeserializeObject<Weather[]>(jsonResult);
            weatherType = deserializedClass[0].main;
        }
        //An error catch, that changes the value of the bool failed, to true. So that we can display an error message
        catch (JsonReaderException)
        {
            failed = true;
        }
    }
}
//Making a public Main class for the json response of the API
public class Weather
{
    public string main { get; set; }
    public string description { get; set; }
}
//Maing a root class for deserialization
public class Root
{
    public Weather weather { get; set; }
}


