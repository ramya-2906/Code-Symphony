        if(s[i]!=s[j]){
            i++;j++;

        }
        else{
            s.erase(i,2);
            
            i=0;j=1;

        }

    }
    return s;

    
}