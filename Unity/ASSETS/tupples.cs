using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class tupples : MonoBehaviour
{
  
    void Start()
    {
        string taskagitmakas(string bir, string iki)
            => (bir, iki) switch
            {

                ("tas", "kagit") => "Kaðýt Kazandý",
                ("tas", "makas") => "Taþ Kazandý",
                ("kagit", "tas") => "Kaðýt Kazandý",
                ("kagit", "makas") => "Makas Kazandý",
                ("makas", "tas") => "Taþ Kazandý",
                ("makas", "kagit") => "Makas Kazandý",
                ("tas","tas") => "Berabere",
                ("makas", "makas") => "Berabere",
                ("kagýt", "kagýt") => "Berabere",
                (_,_) => "Deðerler Boþ"
                

            };

        Debug.Log(taskagitmakas("kagit", "makas"));
        

    }

    
   
}
