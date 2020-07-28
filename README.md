# secret-detection
Finding your secret(Credential, API Key, AWS Key, Token, etc.)  in your source code, files
## Welcome to join in and feel free to contribute.

# USAGE:  
```python3 secret-detection.py --rule /path/to/pattern.json --path /path/to/scan```  
```Ex: python3 secret-detection.py --rule pattern.json --path test/```  

* The ignored list: add patterns for filenames that you want to ignore. Default: ```ignored = ['.git', 'node_modules', 'bower_components', '.sass-cache', '.png', '.ico', '.mov', '.jpeg', 'jpg', '.avi', '.gif', '.apk', '.exe', '.jar', '.dmg', '.pdf', '.ipa', '.svg']```

## OUTPUT
```Filepath: test/test.txt : Line 14
Reason: API KEY

<string name="newrelic_key">HSUFAHSIUYCd7491274LFCAdgdsdgdgdgasdg</string>
~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~
Filepath: test/test.txt : Line 18
Reason: Sendgrid API

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
~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~
Filepath: test/test.txt : Line 20
Reason: Sendgrid API

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
~~~~~~~~~~~~~~~~~~~~~

```

### You also can integrate the tool into CI/CD pipeline  

# Wish List:  
1. Json Ouput  
2. Entropy  
3. Integrate to Git 
4. ...
