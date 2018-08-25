import React, { Component, Fragment } from 'react';
import autoBind from 'react-autobind';
import Tab from '@material-ui/core/Tab';
import Tabs from '@material-ui/core/Tabs';
import Grid from '@material-ui/core/Grid';
import _ from 'lodash';

export default class TabbedList extends Component {
  constructor(props) {
    super(props);
    autoBind(this);
    this.state = { selectedTabIndex: 0 };
  }

  changeTab(event, value) {
    this.setState({ selectedTabIndex: value });
  }

  render() {
    const { children, classes, tabNames } = this.props;
    const { selectedTabIndex } = this.state;

    const header = children[0];
    const tabItems = children.slice(1);

    return (
      <Fragment>
        <Grid item className={classes.caption} xs={12} sm={12} md={12} lg={12}>
          { header }
        </Grid>
        <Grid item className={classes.captionTop} xs={12} sm={12} md={12} lg={12}>
          <Tabs value={selectedTabIndex} onChange={this.changeTab} >
            {
              _.map(tabNames, (label, idx) =>
                <Tab disableRipple label={label} className={classes.tab} key={idx} />
              )
            }
          </Tabs>
        </Grid>
        { tabItems[selectedTabIndex] }
      </Fragment>
    );
  }
}