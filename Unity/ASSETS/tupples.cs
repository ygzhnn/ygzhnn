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

                ("tas", "kagit") => "Ka��t Kazand�",
                ("tas", "makas") => "Ta� Kazand�",
                ("kagit", "tas") => "Ka��t Kazand�",
                ("kagit", "makas") => "Makas Kazand�",
                ("makas", "tas") => "Ta� Kazand�",
                ("makas", "kagit") => "Makas Kazand�",
                ("tas","tas") => "Berabere",
                ("makas", "makas") => "Berabere",
                ("kag�t", "kag�t") => "Berabere",
                (_,_) => "De�erler Bo�"
                

            };

        Debug.Log(taskagitmakas("kagit", "makas"));
        

    }

    
   
}
