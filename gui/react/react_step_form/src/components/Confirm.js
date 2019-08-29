import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import {List, ListItem} from 'material-ui/List';
import RasisedButton from 'material-ui/RaisedButton';

export class confirm extends Component {
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
        const { values:{sysCode, LastName, attributeName, typeSize, description, example } } = this.props;
        return (
            <MuiThemeProvider>
               <React.Fragment>
                   <AppBar title="Confirm Atrribute Data" />
                   <list>
                        <ListItem 
                            primaryText="First name"
                            secondaryText={sysCode}

                        />
                        <ListItem 
                            primaryText="Last name"
                            secondaryText={LastName}
                            
                        />
                        <ListItem 
                            primaryText="attributeName"
                            secondaryText={attributeName}
                            
                        />
                        <ListItem 
                            primaryText="Type"
                            secondaryText={typeSize}
                            
                        />
                        <ListItem 
                            primaryText="Desciption"
                            secondaryText={description}
                            
                        />  
                        <ListItem 
                            primaryText="Example"
                            secondaryText={example}
                            
                        />
                   </list>
                   <br />
                   <RasisedButton 
                        label=" Confirm & Continue "
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
export default confirm;
