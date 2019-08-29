import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import TextField from 'material-ui/TextField';
import RasisedButton from 'material-ui/RaisedButton';

export class FormPersonalDetails extends Component {
    continue = e=> {
        e.preventDefault();
        // Send your data with the API //
        this.props.nextStep();
    }
    back = e=> {
        e.preventDefault();
        this.props.prevStep();
    }
    render() {
        const { values, handleChange } = this.props;
        return (
            <MuiThemeProvider>
               <React.Fragment>
                   <AppBar title="Dictionary - Attribute Detail" />
                   <TextField 
                        hintText="Enter type and size"
                        floatingLabelText="Type"
                        onChange={handleChange("typeSize")}
                        defaultValue={values.typeSize}
                   />
                   <br/>
                   <TextField 
                        hintText="Enter brief description"
                        floatingLabelText="Desciption"
                        onChange={handleChange("description")}
                        defaultValue={values.description}
                   />
                   <br/>
                   <TextField 
                        hintText="Enter example"
                        floatingLabelText="Example"
                        onChange={handleChange("example")}
                        defaultValue={values.example}
                   />   
                   <br/>
                   <RasisedButton 
                        label=" Continue "
                        primary={true}
                        style={StyleSheet.button}
                        onClick={this.continue}
                   />

                   <RasisedButton 
                        label=" Back "
                        primary={false}
                        style={StyleSheet.button}
                        onClick={this.back}
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
export default FormPersonalDetails;