<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:template match="/">GroupID,SSN,FirstName,LastName,Gender,DOB,Address,Address2,City,State,ZIP,Country,HireDate,TerminationDate,Class,Division,Pay Frequency,Status,Benefit,PlanStart,Type,Relation,EnrollmentType,StartDate,Email, Phone, Payroll Group,Employee Id,End Date,Plan,Current Election,YearlyER Amount,Per Pay
       <xsl:for-each  select="//Data//Companies//Company//Employees//Employee//Enrollments//Enrollment">
   <xsl:value-of select="@id"/>
    <xsl:if test="Type='Flexible Spending Account'">
 <!--<xsl:value-of select="concat(../../CompanyIdentifier,',',../../SSN,',',../../FirstName,',',../../LastName,',',Benefit,',',Type,',','0',',',EnrollmentType,',',StartDate,',',EndDate,',')"/>
-->
    <xsl:value-of select="concat(../../CompanyIdentifier,',',../../SSN,',',../../FirstName,',',../../LastName,',',../../Gender,',',../../DOB,',',../../Address1,',',../../Address2,',',../../City,',',../../State,',',../../ZIP,',',../../Country,',',../../HireDate,',',../../TerminationDate,',',../../Class,',',../../Division,',',../../PayFrequency,',',../../EmploymentStatus,',',Benefit,',',PlanStarts,',',Type,',','0',',',EnrollmentType,',',StartDate,',',../../Email,',',../../Phone,',',../../PayrollGroup,',',../../ExternalEmployeeId,',',EndDate,',',Plan,',')"/>
     <xsl:value-of select="CafeteriaData//AnnualAmount"/>
     <xsl:text>, </xsl:text>
         <xsl:text>, </xsl:text>
     <xsl:value-of select="CafeteriaData//PerPayAmount"/>
   <xsl:text>&#xa;</xsl:text>
   </xsl:if>
 <xsl:if test=" Type='Dependent Care Spending Account' or Type='Limited Purpose FSA'">
 <!--<xsl:value-of select="concat(../../CompanyIdentifier,',',../../SSN,',',../../FirstName,',',../../LastName,',',Benefit,',',Type,',','0',',',EnrollmentType,',',StartDate,',',EndDate,',')"/>
-->
    <xsl:value-of select="concat(../../CompanyIdentifier,',',../../SSN,',',../../FirstName,',',../../LastName,',',../../Gender,',',../../DOB,',',../../Address1,',',../../Address2,',',../../City,',',../../State,',',../../ZIP,',',../../Country,',',../../HireDate,',',../../TerminationDate,',',../../Class,',',../../Division,',',../../PayFrequency,',',../../EmploymentStatus,',',Benefit,',',PlanStarts,',',Type,',','0',',',EnrollmentType,',',StartDate,',',../../Email,',',../../Phone,',',../../PayrollGroup,',',../../ExternalEmployeeId,',',EndDate,',',Plan,',')"/>
     <xsl:value-of select="CafeteriaData//AnnualAmount"/>
     <xsl:text>, </xsl:text>
      <xsl:text>, </xsl:text>
     <xsl:value-of select="CafeteriaData//PerPayAmount"/>
   <xsl:text>&#xa;</xsl:text>
   </xsl:if>
           <xsl:if test=" Type='Universal'">
 <!--<xsl:value-of select="concat(../../CompanyIdentifier,',',../../SSN,',',../../FirstName,',',../../LastName,',',Benefit,',',Type,',','0',',',EnrollmentType,',',StartDate,',',EndDate,',')"/>
-->
    <xsl:value-of select="concat(../../CompanyIdentifier,',',../../SSN,',',../../FirstName,',',../../LastName,',',../../Gender,',',../../DOB,',',../../Address1,',',../../Address2,',',../../City,',',../../State,',',../../ZIP,',',../../Country,',',../../HireDate,',',../../TerminationDate,',',../../Class,',',../../Division,',',../../PayFrequency,',',../../EmploymentStatus,',',Benefit,',',PlanStarts,',',Type,',','0',',',EnrollmentType,',',StartDate,',',../../Email,',',../../Phone,',',../../PayrollGroup,',',../../ExternalEmployeeId,',',EndDate,',',Plan,',')"/>
     <xsl:value-of select="BenefitAmount"/>
     <xsl:text>, </xsl:text>
      <xsl:text>, </xsl:text>
     <xsl:value-of select="EmployeeCost"/>
   <xsl:text>&#xa;</xsl:text>
   </xsl:if>
</xsl:for-each>

   </xsl:template>
</xsl:stylesheet>