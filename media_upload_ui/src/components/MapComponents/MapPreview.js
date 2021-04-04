import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import Card from '@material-ui/core/Card';

const useStyles = makeStyles({
    root: {
      minWidth: 275,
    },
    title: {
      fontSize: 14,
    },
  });

export default function Preview({previews}) {
    const classes = useStyles();
    return (
        <>
        { previews.map(( preview, key ) => (
            <Card key={preview.map_id}>
              <CardContent>
                <Typography className={classes.title} color="textSecondary" gutterBottom>
                  {preview.filename}
                </Typography>
                <Typography variant="h5" component="h2">
                  {preview.name}
                </Typography>
                <Typography variant="body2" component="p">
                  {preview.upload_dt}
                </Typography>
              </CardContent>
            </Card>
        
        ))}
        </>
    )
}