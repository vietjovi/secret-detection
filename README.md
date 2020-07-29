# secret-detection
secret-detection is a static code analysis tool designed for parsing various common data formats in search of hardcoded credentials and sensitive information. secret-detection can run in the CLI or you can integrate it in your CI/CD pipeline.

## Feature
* Using regex rules to scan, and help identify the following types of secrets:
    * API Keys
    * AWS Keys
    * OAuth Client Secrets
    * SSH Private Keys
    * ...
 * Supports a whitelisted
 * Supports custom rules
 * Lightweight
 * Easy to customize to your needs 

## Welcome to join in and feel free to contribute.

## USAGE  
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

## Wish List:  
1. Json Ouput  
2. Entropy  
3. Integrate to Git 
4. ...

## License
### This project is licensed under the terms of the MIT license.
