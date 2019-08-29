import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import TextField from 'material-ui/TextField';
import RasisedButton from 'material-ui/RaisedButton';

export class FormUserDetails extends Component {
    continue = e=> {
        e.preventDefault();
        this.props.nextStep();
    }
    render() {
        const { values, handleChange } = this.props;
        return (
            <MuiThemeProvider>
               <React.Fragment>
                   <AppBar title="Dictionary - Attribute Configuration" />
                   <TextField 
                        hintText="Enter system code"
                        floatingLabelText="System code"
                        onChange={handleChange("sysCode")}
                        defaultValue={values.sysCode}
                   />
                   <br/>
                   <TextField 
                        hintText="Enter table name"
                        floatingLabelText="Table name"
                        onChange={handleChange("tableName")}
                        defaultValue={values.tableName}
                   />
                   <br/>
                   <TextField 
                        hintText="Enter attribute name"
                        floatingLabelText="Attribute name"
                        onChange={handleChange("attributeName")}
                        defaultValue={values.attributeName}
                   />   
                   <br/>
                   <RasisedButton 
                        label="Continue"
                        primary={true}
                        style={StyleSheet.button}
                        onClick={this.continue}
                   />                
                </React.Fragment>
            </MuiThemeProvider>
        );
    }
}

const styles = {
    button: {
        margin:15
    }
}
export default FormUserDetails;