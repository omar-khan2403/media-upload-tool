import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';

const useStyles = makeStyles({
    root: {
      minWidth: 275,
    },
  });

export default function Preview({previews}) {
    const classes = useStyles();
    return (
        <>
        { previews.map(( preview, key ) => (
            <Card>

            </Card>
        
        ))}
        </>
    )
}