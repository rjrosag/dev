from dicEnvironment import Sysenv
from shutil import copyfile

class GUIReact:
    def __init__(self):
        self.userForms = ["UserForm.js", "FormUserDetails.js", "FormPersonalDetails.js", "Confirm.js"]

    def Backup(self, path="react_step_form//public//", filename="index.html" ):
        Sys = Sysenv()
        status = True

        # Check if index.tmpl not exist make a copy of the original file index.html to index.tmpl
        sourceFilepath= Sys.getPathReact() + path
        sourceFile = Sys.getPathReact() + path + filename
        targetFile = Sys.getPathReact() + path + filename + "_tmpl"

        if not Sys.find(filename + "_tmpl", sourceFilepath ):
            try:
                copyfile(sourceFile, targetFile)
            except IOError as e:
                print("Unable to copy the file %s" % e)
                status = False
        return(status)

    # Set the files to template style
    def Restore(self, path="react_step_form//public//"):
        Sys = Sysenv()
        status = True

        # Check if index.tmpl not exist make a copy of the template file index.html_tmpl to index.js
        sourceFilepath = Sys.getPathReact() + path

        for filename in self.userForms:
            sourceFile = Sys.getPathReact() + path + filename + "_tmpl"
            targetFile = Sys.getPathReact() + path + filename

            if not Sys.find(filename + "_tmpl", sourceFilepath):
                try:
                    copyfile(sourceFile, targetFile)
                except IOError as e:
                    print("Unable to copy the file %s" % e)
                    status = False
        return (status)


    # Change Browser tab title @ %HOME/dev/gui/react/react_step_form/public/index.html - React App with your system title
    def setTitle(self, title="" ):
        status = True
        if not title:
            return (status)
        Sys = Sysenv()
        path = "react_step_form//public//"
        filename = "index.html"
        sourceFile = Sys.getPathReact() + path + filename
        s = ""
        if self.Backup(path, filename):
            with open(sourceFile, 'r') as file:
                s = file.read()
                if '<title>React App</title>' in s:
                    s = s.replace('<title>React App</title>', title)
            if s:
                with open(sourceFile, 'w') as file:
                    file.write(s)
            else:
                status=False
        return (status)

    def setAttribute(self, pattern="", target="" ):
        status = True
        if not target or not pattern:
            return (status)
        Sys = Sysenv()
        path = "react_step_form//src//components//"
        for filename in self.userForms:
            sourceFile = Sys.getPathReact() + path + filename
            s = ""
            if self.Backup(path, filename):
                with open(sourceFile, 'r') as file:
                    s = file.read()
                    if pattern in s:
                        s = s.replace(pattern, target)
                    if s:
                        with open(sourceFile, 'w') as file:
                            file.write(s)
                    else:
                        status=False
        return (status)

'''
Fill out section below and run find replace command.  This GUI is set to manager 6 fields and w2 windows; 3 per windows
 {"FormTitle1" : "Dictionary - Attribute Configuration",
 "FormTitle2" : "Dictionary - Attribute Detail",
 "FormTitle3" : "Confirm Atrribute Data"
 "newfield1_floatlabel" : "System code",
 "newfield2_floatlabel" : "Table name",
 "newfield3_floatlabel" : "Attribute name",
 "newfield4_floatlabel" : "Type",
 "newfield5_floatlabel" : "Desciption",
 "newfield6_floatlabel" : "Example",
 
 "newfield1_label" : "Enter system code",
 "newfield2_label" : "Enter table name",
 "newfield3_label" : "Enter attribute name",
 "newfield4_label" : "Enter type and size",
 "newfield5_label" : "Enter brief description",
 "newfield6_label" : "Enter example",
 
 "newfield1" : "sysCode",
 "newfield2" : "tableName",
 "newfield3" : "attributeName",
 "newfield4" : "typeSize",
 "newfield5" : "description",
 "newfield6" : "example",
 }
 '''
sysreact= GUIReact()
sysreact.setTitle('<title>Social Community</title>')

# Check if UserForm.tmpl exist if not Make a copy of the original file UserForm.js to UserForm.tmpl
''' Change the following fields in file %HOME/dev/gui/react/react_step_form/src/components/UserForm.js,
        firstName:"",
        lastName:"",
        email:"",
        occupation:"",
        city:"",
        bio:""
'''
sysreact.setAttribute('firstName', 'sysCode')
sysreact.setAttribute('lastName', 'tableName')
sysreact.setAttribute('email', 'attributeName')
sysreact.setAttribute('occupation', 'typeSize')
sysreact.setAttribute('city', 'description')
sysreact.setAttribute('bio', 'example')

# Check if FormUserDetails.tmpl exist if not Make a copy of the original file FormUserDetails.js to FormUserDetails.tmpl
''' Change the following fields in file %HOME/dev/gui/react/react_step_form/src/components/FormUserDetails.js,
        title="EnterUser Details",
        hintText="Enter Your First Name",
        hintText="Enter Your Last Name"
        floatingLabelText="Last Name"
        hintText="Enter Your e-mail"
        floatingLabelText="e-mail"
        label="Continue"
'''
# Labels
sysreact.setAttribute("EnterUser Details", "Dictionary - Attribute Configuration")
sysreact.setAttribute("Enter Your First Name", "Enter system code")
sysreact.setAttribute("Enter Your Last Name", "Enter table name")
sysreact.setAttribute("Enter Your e-mail", "Enter attribute name")
sysreact.setAttribute("First Name", "System code")
sysreact.setAttribute("Last Name", "Table name")
sysreact.setAttribute("e-mail", "Attribute name")


# Check if FormPersonalDetails.tmpl exist if not Make a copy of the original file FormPersonalDetails.js to FormPersonalDetails.tmpl
''' Change the following fields in file %HOME/dev/gui/react/react_step_form/src/components/FormPersonalDetails.js,
    <AppBar title="Enter Personal Details" />
    hintText="Enter Your Occupation"
    floatingLabelText="Occupation"
    onChange={handleChange("occupation")}
    defaultValue={values.occupation}
    hintText="Enter Your City"
    floatingLabelText="City"
    onChange={handleChange("city")}
    defaultValue={values.city}
    hintText="Enter Your Bio"
    floatingLabelText="Bio"
    onChange={handleChange("bio")}
    defaultValue={values.bio}
    label=" Continue "
    onClick={this.continue}
    label=" Back "
    onClick={this.back}
'''
sysreact.setAttribute("Enter Personal Details", "Dictionary - Attribute Detail")
sysreact.setAttribute("Enter Your Occupation", "Enter type and size")
sysreact.setAttribute("Enter Your City", "Enter brief description")
sysreact.setAttribute("Enter Your Bio", "Enter example")
sysreact.setAttribute("Occupation", "Type")
sysreact.setAttribute("City", "Desciption")
sysreact.setAttribute("Bio", "Example")


# Check if Confirm.tmpl exist if not Make a copy of the original file Confirm.js to Confirm.tmpl
''' Change the following fields in file %HOME/dev/gui/react/react_step_form/src/components/Confirm.js,
    const { values:{firstName, LastName, email, occupation, city, bio } } = this.props;
    <AppBar title="Confirm User Data" />
    primaryText="First name"
    secondaryText={firstName}
    primaryText="Last name"
    secondaryText={LastName}
    primaryText="email address"
    secondaryText={email}
    primaryText="Job"
    secondaryText={occupation}
    primaryText="City"
    secondaryText={city}
    primaryText="Bio"
    secondaryText={bio}
    label=" Confirm & Continue "
    onClick={this.continue}
    label="Back"
    onClick={this.back}
'''
sysreact.setAttribute("Confirm User Data", "Confirm Attribute Data")
sysreact.setAttribute("email", "Attribute name")
sysreact.setAttribute("Job", "Type")
sysreact.setAttribute("Bio", "Example")

# Check if Success.tmpl exist if not Make a copy of the original file Success.js to Success.tmpl
''' Change the following fields in file %HOME/dev/gui/react/react_step_form/src/components/Success.js,
    <AppBar title="Success!" />
    <h1>Thank you for your submission </h1>
    <p>You will get an e-mail with further instructions</p>
'''